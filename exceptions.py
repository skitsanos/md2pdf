"""
Custom exceptions for md2pdf.
"""


class Md2PdfError(Exception):
    """Base exception for all md2pdf errors."""
    pass


class FileValidationError(Md2PdfError):
    """Raised when file validation fails."""
    pass


class StyleError(Md2PdfError):
    """Raised when style loading or processing fails."""
    pass


class ConversionError(Md2PdfError):
    """Raised when PDF conversion fails."""
    pass


class TemplateError(Md2PdfError):
    """Raised when template loading or rendering fails."""
    pass


class SecurityError(Md2PdfError):
    """Raised when security validation fails."""
    pass