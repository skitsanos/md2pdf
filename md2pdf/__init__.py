"""
Markdown to PDF CLI Tool

A Python CLI tool that converts one or more Markdown documents 
into a single PDF file with customizable CSS styling.
"""

__version__ = "1.0.0"
__author__ = "Manus AI"
__description__ = "Convert Markdown documents to PDF with customizable styling"


def main(*args, **kwargs):
    """Lazy CLI import to avoid hard runtime dependency during library-only imports."""
    from .cli import main as cli_main
    return cli_main(*args, **kwargs)


def __getattr__(name):
    if name == "MarkdownToPDFConverter":
        from .converter import MarkdownToPDFConverter
        return MarkdownToPDFConverter
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__all__ = ['main', 'MarkdownToPDFConverter', '__version__', '__author__', '__description__']
