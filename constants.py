"""
Constants and configuration values for md2pdf.
"""

# File extensions
MARKDOWN_EXTENSIONS = frozenset(['.md', '.markdown'])

# CSS units
VALID_CSS_UNITS = frozenset(['mm', 'cm', 'in', 'px', 'pt', 'pc'])

# Default values
DEFAULT_MARGIN = "20mm"
DEFAULT_PAGE_SIZE = "A4"
DEFAULT_STYLE = "default"

# Supported page sizes
VALID_PAGE_SIZES = frozenset([
    'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
    'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
    'Letter', 'Legal', 'Ledger', 'Tabloid', 'Executive'
])

# Character encoding attempts
ENCODING_ATTEMPTS = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']

# Markdown extensions configuration
MARKDOWN_EXTENSIONS_LIST = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code'
]

MARKDOWN_EXTENSION_CONFIGS = {
    'markdown.extensions.codehilite': {
        'css_class': 'highlight',
        'use_pygments': True
    },
    'markdown.extensions.toc': {
        'permalink': False
    }
}

# Style descriptions
BUILTIN_STYLE_DESCRIPTIONS = {
    'default': 'Clean, readable style with good typography',
    'github': 'GitHub-flavored styling with familiar appearance',
    'minimal': 'Minimal design with focus on content',
    'academic': 'Professional academic paper style',
    'modern': 'Contemporary design with modern typography',
    'dark': 'Dark mode theme for reduced eye strain',
    'technical': 'Technical documentation with monospaced fonts',
    'book': 'Classic book typography with elegant serif fonts',
    'presentation': 'Large fonts optimized for presentations'
}