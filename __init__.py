"""
Markdown to PDF CLI Tool

A Python CLI tool that converts one or more Markdown documents 
into a single PDF file with customizable CSS styling.
"""

__version__ = "1.0.0"
__author__ = "Manus AI"
__description__ = "Convert Markdown documents to PDF with customizable styling"

from .cli import main
from .converter import MarkdownToPDFConverter

__all__ = ['main', 'MarkdownToPDFConverter', '__version__', '__author__', '__description__']

