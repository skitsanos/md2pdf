"""
Command Line Interface for the Markdown to PDF converter.
"""

import click
import sys
from pathlib import Path

from .converter import MarkdownToPDFConverter
from .utils import validate_input_files, validate_output_path, parse_margin
from .constants import DEFAULT_MARGIN, DEFAULT_PAGE_SIZE, DEFAULT_STYLE
from .exceptions import Md2PdfError, FileValidationError

__version__ = "1.0.0"  # Define version here to avoid circular import


@click.command()
@click.argument('input_files', nargs=-1, required=True, type=str)
@click.option(
    '--output', '-o',
    required=True,
    type=str,
    help='Output PDF file path (required)'
)
@click.option(
    '--style', '-s',
    default=DEFAULT_STYLE,
    type=str,
    help='CSS styling options: path to custom CSS file or built-in style name (github, minimal, academic, default)'
)
@click.option(
    '--title',
    type=str,
    help='Set PDF document title (defaults to first heading or filename)'
)
@click.option(
    '--margin',
    default=DEFAULT_MARGIN,
    type=str,
    help='Set page margins (e.g., "20mm", "1in"). Default: 20mm'
)
@click.option(
    '--page-size',
    default=DEFAULT_PAGE_SIZE,
    type=str,
    help='Specify page size (A4, Letter, Legal, etc.). Default: A4'
)
@click.option(
    '--toc/--no-toc',
    default=False,
    help='Generate table of contents. Default: disabled'
)
@click.option(
    '--merge/--no-merge',
    default=True,
    help='How to handle multiple files: merge with separators or start each file on a new page. Default: merge'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Enable verbose output for debugging'
)
@click.version_option(version=__version__, prog_name='md2pdf')
def main(
    input_files: tuple,
    output: str,
    style: str,
    title: str,
    margin: str,
    page_size: str,
    toc: bool,
    merge: bool,
    verbose: bool
):
    """
    Convert one or more Markdown documents into a single PDF file with customizable CSS styling.
    
    INPUT_FILES: One or more Markdown files or glob patterns (e.g., *.md, docs/*.md)
    
    Examples:
    
    \b
    # Basic usage
    md2pdf document.md --output report.pdf
    
    \b
    # Multiple files
    md2pdf intro.md chapter1.md chapter2.md --output book.pdf
    
    \b
    # With custom styling
    md2pdf *.md --output styled-doc.pdf --style custom.css
    
    \b
    # Using built-in styles
    md2pdf README.md --output readme.pdf --style github
    
    \b
    # With table of contents and custom title
    md2pdf docs/*.md --output manual.pdf --style academic --toc --title "User Manual"
    """
    try:
        # Validate input files
        if verbose:
            click.echo(f"Validating {len(input_files)} input pattern(s)...")
        
        validated_files = validate_input_files(list(input_files))
        
        if verbose:
            click.echo(f"Found {len(validated_files)} Markdown file(s):")
            for file_path in validated_files:
                click.echo(f"  - {file_path}")
        
        # Validate output path
        output_path = validate_output_path(output)
        
        if verbose:
            click.echo(f"Output will be saved to: {output_path}")
        
        # Validate margin format
        try:
            validated_margin = parse_margin(margin)
        except ValueError as e:
            raise click.BadParameter(str(e), param_hint=['--margin'])
        
        # Initialize converter
        converter = MarkdownToPDFConverter(verbose=verbose)
        
        # Perform conversion
        converter.convert_files_to_pdf(
            input_files=validated_files,
            output_path=output_path,
            style=style,
            title=title,
            margin=validated_margin,
            page_size=page_size,
            generate_toc=toc,
            merge_files=merge,
            verbose=verbose
        )
        
        # Success message
        if not verbose:
            click.echo(f"✓ PDF created successfully: {output_path}")
        
    except (FileNotFoundError, FileValidationError, ValueError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Md2PdfError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        if verbose:
            import traceback
            click.echo(f"Unexpected error: {e}", err=True)
            click.echo(traceback.format_exc(), err=True)
        else:
            click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@click.group()
def cli():
    """Markdown to PDF CLI Tool"""
    pass


# Removed unused CLI group and subcommands - these were never accessible from main()


# Make main the default command when called directly
if __name__ == '__main__':
    main()
