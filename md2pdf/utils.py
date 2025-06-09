"""
Utility functions for the Markdown to PDF converter.
"""

import os
import glob
from pathlib import Path
from typing import List
from .constants import MARKDOWN_EXTENSIONS, ENCODING_ATTEMPTS
from .exceptions import FileValidationError
from .validators import validate_margin as validate_margin_format


def validate_input_files(file_patterns: List[str]) -> List[Path]:
    """
    Validate and expand input file patterns to actual file paths.
    
    Args:
        file_patterns: List of file paths or glob patterns
        
    Returns:
        List of validated Path objects
        
    Raises:
        FileNotFoundError: If no files match the patterns
        ValueError: If files are not readable
    """
    all_files = []
    
    for pattern in file_patterns:
        # Expand glob patterns
        if '*' in pattern or '?' in pattern:
            matched_files = glob.glob(pattern)
            if not matched_files:
                raise FileNotFoundError(f"No files found matching pattern: {pattern}")
            all_files.extend(matched_files)
        else:
            # Single file
            if not os.path.exists(pattern):
                raise FileNotFoundError(f"File not found: {pattern}")
            all_files.append(pattern)
    
    # Convert to Path objects and validate
    validated_files = []
    for file_path in all_files:
        path_obj = Path(file_path)
        if not path_obj.is_file():
            raise FileValidationError(f"Not a file: {file_path}")
        if path_obj.suffix.lower() not in MARKDOWN_EXTENSIONS:
            raise FileValidationError(f"Not a Markdown file: {file_path}")
        if not os.access(path_obj, os.R_OK):
            raise FileValidationError(f"File not readable: {file_path}")
        validated_files.append(path_obj)
    
    return validated_files


def validate_output_path(output_path: str) -> Path:
    """
    Validate the output PDF path.
    
    Args:
        output_path: Path for the output PDF file
        
    Returns:
        Validated Path object
        
    Raises:
        ValueError: If output path is invalid
    """
    path_obj = Path(output_path)
    
    # Ensure .pdf extension
    if path_obj.suffix.lower() != '.pdf':
        path_obj = path_obj.with_suffix('.pdf')
    
    # Check if parent directory exists and is writable
    parent_dir = path_obj.parent
    if not parent_dir.exists():
        try:
            parent_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise ValueError(f"Cannot create output directory: {e}")
    
    if not os.access(parent_dir, os.W_OK):
        raise ValueError(f"Output directory not writable: {parent_dir}")
    
    return path_obj


def read_file_content(file_path: Path) -> str:
    """
    Read the content of a file with proper encoding handling.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        File content as string
        
    Raises:
        UnicodeDecodeError: If file encoding is not supported
    """
    encodings = ENCODING_ATTEMPTS
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    
    attempted = ', '.join(encodings)
    raise UnicodeDecodeError(
        f"Could not decode file {file_path}. Attempted encodings: {attempted}"
    )


def parse_margin(margin_str: str) -> str:
    """
    Parse and validate margin specification.
    
    Args:
        margin_str: Margin specification (e.g., "20mm", "1in", "15px")
        
    Returns:
        Validated margin string
        
    Raises:
        ValueError: If margin format is invalid
    """
    from .constants import DEFAULT_MARGIN
    
    if not margin_str:
        return DEFAULT_MARGIN
    
    return validate_margin_format(margin_str)


def generate_toc_from_html(html_content: str) -> str:
    """
    Generate table of contents from HTML headings.
    
    Args:
        html_content: HTML content to extract headings from
        
    Returns:
        HTML string containing the table of contents
    """
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    if not headings:
        return ""
    
    toc_html = "<ul class='toc-list'>\n"
    
    for i, heading in enumerate(headings):
        level = int(heading.name[1])  # Extract number from h1, h2, etc.
        text = heading.get_text().strip()
        
        # Create anchor ID
        anchor_id = f"toc-{i}"
        heading['id'] = anchor_id
        
        # Add to TOC with proper indentation
        indent = "  " * (level - 1)
        toc_html += f"{indent}<li class='toc-level-{level}'><a href='#{anchor_id}'>{text}</a></li>\n"
    
    toc_html += "</ul>\n"
    
    return toc_html

