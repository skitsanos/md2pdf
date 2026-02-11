"""
Core Markdown to PDF conversion functionality.
"""

import markdown
import weasyprint
from pathlib import Path
from typing import List, Optional
from jinja2 import Template, TemplateError as JinjaTemplateError

from .utils import read_file_content, generate_toc_from_html
from .styles import get_builtin_style, load_custom_style
from .constants import (
    MARKDOWN_EXTENSIONS_LIST, MARKDOWN_EXTENSION_CONFIGS,
    DEFAULT_MARGIN, DEFAULT_PAGE_SIZE, DEFAULT_STYLE
)
from .exceptions import ConversionError, TemplateError, StyleError
from .validators import sanitize_html, validate_css_file_path, validate_page_size
from .logger import LoggerMixin


class MarkdownToPDFConverter(LoggerMixin):
    """Main converter class for Markdown to PDF conversion."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the converter with default settings."""
        super().__init__(verbose=verbose)
        self.markdown_extensions = MARKDOWN_EXTENSIONS_LIST
        self.markdown_extension_configs = MARKDOWN_EXTENSION_CONFIGS
    
    def convert_files_to_pdf(
        self,
        input_files: List[Path],
        output_path: Path,
        style: Optional[str] = None,
        title: Optional[str] = None,
        margin: str = DEFAULT_MARGIN,
        page_size: str = DEFAULT_PAGE_SIZE,
        generate_toc: bool = False,
        merge_files: bool = True,
        verbose: bool = False
    ) -> None:
        """
        Convert Markdown files to PDF.
        
        Args:
            input_files: List of input Markdown file paths
            output_path: Output PDF file path
            style: Style name or path to custom CSS file
            title: Document title (defaults to first heading or filename)
            margin: Page margins (e.g., "20mm")
            page_size: Page size (A4, Letter, etc.)
            generate_toc: Whether to generate table of contents
            merge_files: Whether to merge multiple files into one document
            verbose: Enable verbose output
        """
        if verbose:
            self.logger.info(f"Converting {len(input_files)} file(s) to PDF...")
        
        # Validate page size
        try:
            page_size = validate_page_size(page_size)
        except ValueError as e:
            raise ConversionError(f"Invalid page size: {e}")
        
        # Read and convert Markdown files
        html_content = self._process_markdown_files(input_files, merge_files)
        
        # Determine document title
        if not title:
            title = self._extract_title_from_html(html_content) or input_files[0].stem
        
        # Load CSS styles
        css_content = self._load_styles(style)
        
        # Generate table of contents if requested
        toc_content = ""
        if generate_toc:
            toc_content = generate_toc_from_html(html_content)
            if toc_content:
                self.logger.debug("Generated table of contents")
        
        # Create final HTML document
        final_html = self._create_html_document(
            content=html_content,
            css_content=css_content,
            title=title,
            toc_content=toc_content,
            generate_toc=generate_toc
        )
        
        # Convert to PDF
        self._html_to_pdf(
            html_content=final_html,
            output_path=output_path,
            margin=margin,
            page_size=page_size
        )
        
        if verbose:
            self.logger.info(f"PDF successfully created: {output_path}")
    
    def _process_markdown_files(
        self, 
        input_files: List[Path], 
        merge_files: bool
    ) -> str:
        """Process Markdown files and convert to HTML."""
        md = markdown.Markdown(
            extensions=self.markdown_extensions,
            extension_configs=self.markdown_extension_configs
        )
        
        html_parts = []
        
        for i, file_path in enumerate(input_files):
            self.logger.debug(f"Processing: {file_path}")
            
            # Read file content
            content = read_file_content(file_path)
            
            # Convert to HTML
            html = md.convert(content)
            
            # For multiple input files, either visually merge with separators
            # or force each file to start on a new page.
            if i > 0:
                if merge_files:
                    html_parts.append('<div class="file-separator"></div>')
                else:
                    html_parts.append('<div class="page-break"></div>')
            
            html_parts.append(html)
            
            # Reset markdown instance for next file
            md.reset()
        
        return '\n'.join(html_parts)
    
    @staticmethod
    def _extract_title_from_html(html_content: str) -> Optional[str]:
        """Extract title from the first heading in HTML content."""
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(html_content, 'html.parser')
        first_heading = soup.find(['h1', 'h2', 'h3'])
        
        if first_heading:
            return first_heading.get_text().strip()
        
        return None
    
    def _load_styles(self, style: Optional[str]) -> str:
        """Load CSS styles from built-in styles or custom file."""
        if not style:
            style = DEFAULT_STYLE
        
        try:
            # Check if it's a file path
            if style.endswith('.css'):
                # Validate and load custom CSS
                css_path = validate_css_file_path(style)
                self.logger.debug(f"Loading custom CSS: {css_path}")
                return load_custom_style(str(css_path))
            else:
                # Built-in style
                self.logger.debug(f"Using built-in style: {style}")
                return get_builtin_style(style)
        except Exception as e:
            raise StyleError(f"Failed to load style '{style}': {e}")
    
    @staticmethod
    def _create_html_document(
        content: str,
        css_content: str,
        title: str,
        toc_content: str,
        generate_toc: bool
    ) -> str:
        """Create the final HTML document using the template."""
        template_path = Path(__file__).parent / "templates" / "base.html"
        
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
        except (IOError, OSError) as e:
            raise TemplateError(f"Failed to load HTML template: {e}")
        
        try:
            template = Template(template_content)
            
            # Sanitize content for security
            sanitized_content = sanitize_html(content)
            
            return template.render(
                title=title,
                css_content=css_content,
                content=sanitized_content,
                toc_content=toc_content,
                toc=generate_toc
            )
        except JinjaTemplateError as e:
            raise TemplateError(f"Failed to render template: {e}")
    
    def _html_to_pdf(
        self,
        html_content: str,
        output_path: Path,
        margin: str,
        page_size: str
    ) -> None:
        """Convert HTML to PDF using WeasyPrint."""
        self.logger.debug("Converting HTML to PDF...")
        
        # Configure CSS for page settings
        css_string = f"""
        @page {{
            size: {page_size};
            margin: {margin};
        }}
        .page-break {{
            page-break-before: always;
        }}
        """
        
        try:
            # Create WeasyPrint HTML object
            html_doc = weasyprint.HTML(string=html_content)
            css_doc = weasyprint.CSS(string=css_string)
            
            # Generate PDF
            html_doc.write_pdf(
                target=str(output_path),
                stylesheets=[css_doc]
            )
        except Exception as e:
            raise ConversionError(f"Failed to generate PDF: {e}")
