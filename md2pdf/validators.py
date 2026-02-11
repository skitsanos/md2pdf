"""
Input validation and security checks for md2pdf.
"""

import os
import re
from pathlib import Path
from .constants import VALID_CSS_UNITS, VALID_PAGE_SIZES
from .exceptions import SecurityError, FileValidationError


def sanitize_html(content: str) -> str:
    """
    Basic HTML sanitization to prevent XSS attacks.
    
    Note: This is a basic implementation. For production use,
    consider using a dedicated library like nh3 or html-sanitizer.
    
    Args:
        content: Raw HTML content
        
    Returns:
        Sanitized HTML content
    """
    # For now, we'll trust the markdown converter's output
    # since it's generated from markdown files, not user HTML input
    # If you need stronger sanitization, consider using nh3 or html-sanitizer
    
    # Basic protection: escape script tags and event handlers
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'\bon\w+\s*=\s*["\']?[^"\']*["\']?', '', content, flags=re.IGNORECASE)
    content = re.sub(r'javascript:', '', content, flags=re.IGNORECASE)
    
    return content


def validate_css_file_path(css_path: str) -> Path:
    """
    Validate CSS file path for security issues.
    
    Args:
        css_path: Path to CSS file
        
    Returns:
        Validated Path object
        
    Raises:
        SecurityError: If path contains security risks
        FileValidationError: If file is invalid
    """
    if not css_path or '\x00' in css_path:
        raise SecurityError(f"Invalid CSS file path: {css_path}")

    # Allow both relative and absolute paths, but normalize before validation.
    try:
        resolved_path = Path(css_path).expanduser().resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        raise SecurityError(f"Invalid CSS file path: {css_path}") from exc
    
    # Check file exists and is readable
    if not resolved_path.exists():
        raise FileValidationError(f"CSS file not found: {css_path}")
    
    if not resolved_path.is_file():
        raise FileValidationError(f"Not a file: {css_path}")
    
    if not os.access(resolved_path, os.R_OK):
        raise FileValidationError(f"CSS file not readable: {css_path}")
    
    # Check file extension
    if resolved_path.suffix.lower() != '.css':
        raise FileValidationError(f"Not a CSS file: {css_path}")
    
    return resolved_path


def validate_page_size(page_size: str) -> str:
    """
    Validate page size specification.
    
    Args:
        page_size: Page size string
        
    Returns:
        Validated page size
        
    Raises:
        ValueError: If page size is invalid
    """
    if page_size not in VALID_PAGE_SIZES:
        valid_sizes = ', '.join(sorted(VALID_PAGE_SIZES))
        raise ValueError(f"Invalid page size: {page_size}. Valid sizes are: {valid_sizes}")
    
    return page_size


def validate_margin(margin_str: str) -> str:
    """
    Validate margin specification.
    
    Args:
        margin_str: Margin specification (e.g., "20mm", "1in")
        
    Returns:
        Validated margin string
        
    Raises:
        ValueError: If margin format is invalid
    """
    if not margin_str:
        raise ValueError("Margin cannot be empty")
    
    # Extract number and unit
    pattern = r'^(\d+(?:\.\d+)?)(' + '|'.join(VALID_CSS_UNITS) + ')$'
    match = re.match(pattern, margin_str.lower())
    
    if not match:
        valid_units = ', '.join(VALID_CSS_UNITS)
        raise ValueError(
            f"Invalid margin format: {margin_str}. "
            f"Use format like '20mm', '1in'. Valid units: {valid_units}"
        )
    
    return margin_str.lower()


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to prevent security issues.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove any path components
    filename = os.path.basename(filename)
    
    # Remove potentially dangerous characters
    filename = re.sub(r'[^\w\s.-]', '_', filename)
    
    # Remove multiple consecutive dots
    filename = re.sub(r'\.{2,}', '.', filename)
    
    # Ensure it doesn't start with a dot (hidden file)
    if filename.startswith('.'):
        filename = '_' + filename[1:]
    
    return filename
