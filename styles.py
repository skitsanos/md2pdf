"""
Built-in CSS styles for PDF generation.
"""

from pathlib import Path
from typing import Dict
from .constants import BUILTIN_STYLE_DESCRIPTIONS
from .exceptions import StyleError
try:
    from .yaml_styles import yaml_style_loader
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml_style_loader = None


def get_builtin_style(style_name: str) -> str:
    """
    Get CSS content for a built-in style (includes YAML styles).
    
    Args:
        style_name: Name of the built-in style
        
    Returns:
        CSS content as string
        
    Raises:
        StyleError: If style name is not found
    """
    # First try YAML styles if available
    yaml_styles = {}
    if HAS_YAML and yaml_style_loader:
        yaml_styles = yaml_style_loader.list_yaml_styles()
        if style_name in yaml_styles:
            return yaml_style_loader.load_yaml_style(style_name)
    
    # Then try built-in Python styles
    styles = {
        'default': _get_default_style(),
        'github': _get_github_style(),
        'minimal': _get_minimal_style(),
        'academic': _get_academic_style(),
        'modern': _get_modern_style(),
        'dark': _get_dark_style(),
        'technical': _get_technical_style(),
        'book': _get_book_style(),
        'presentation': _get_presentation_style()
    }
    
    if style_name in styles:
        return styles[style_name]
    
    # Style not found anywhere
    all_styles = list(styles.keys())
    if HAS_YAML:
        all_styles.extend(yaml_styles.keys())
    
    available = ', '.join(sorted(all_styles))
    raise StyleError(f"Unknown style: {style_name}. Available styles: {available}")


def load_custom_style(css_file_path: str) -> str:
    """
    Load CSS content from a custom file.
    
    Args:
        css_file_path: Path to the CSS file
        
    Returns:
        CSS content as string
        
    Raises:
        FileNotFoundError: If CSS file doesn't exist
        ValueError: If file is not readable
    """
    css_path = Path(css_file_path)
    
    if not css_path.exists():
        raise FileNotFoundError(f"CSS file not found: {css_file_path}")
    
    if not css_path.is_file():
        raise StyleError(f"Not a file: {css_file_path}")
    
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        raise StyleError(f"Could not read CSS file {css_file_path}: {e}")


def list_builtin_styles() -> Dict[str, str]:
    """
    Get a dictionary of available built-in styles with descriptions.
    
    Returns:
        Dictionary mapping style names to descriptions
    """
    styles = BUILTIN_STYLE_DESCRIPTIONS.copy()
    
    # Add YAML styles if available
    if HAS_YAML and yaml_style_loader:
        try:
            yaml_styles = yaml_style_loader.list_yaml_styles()
            styles.update(yaml_styles)
        except Exception:
            pass  # Ignore YAML loading errors for style listing
    
    return styles


def _get_default_style() -> str:
    """Default clean and readable style."""
    return """
/* Default Style - Clean and Readable */

/* Base styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    max-width: none;
    margin: 0;
    padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.25;
    margin-top: 24pt;
    margin-bottom: 12pt;
    color: #1a1a1a;
}

h1 {
    font-size: 24pt;
    border-bottom: 2pt solid #eee;
    padding-bottom: 8pt;
}

h2 {
    font-size: 18pt;
    border-bottom: 1pt solid #eee;
    padding-bottom: 6pt;
}

h3 {
    font-size: 14pt;
}

h4 {
    font-size: 12pt;
}

h5, h6 {
    font-size: 11pt;
}

/* Paragraphs */
p {
    margin: 0 0 12pt 0;
    text-align: justify;
}

/* Lists */
ul, ol {
    margin: 12pt 0;
    padding-left: 24pt;
}

li {
    margin: 6pt 0;
}

/* Code */
code {
    font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
    font-size: 10pt;
    background-color: #f6f8fa;
    padding: 2pt 4pt;
    border-radius: 3pt;
    border: 1pt solid #e1e4e8;
}

pre {
    font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
    font-size: 10pt;
    background-color: #f6f8fa;
    padding: 12pt;
    border-radius: 6pt;
    border: 1pt solid #e1e4e8;
    overflow-x: auto;
    margin: 12pt 0;
}

pre code {
    background: none;
    border: none;
    padding: 0;
}

/* Tables */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12pt 0;
}

th, td {
    border: 1pt solid #ddd;
    padding: 8pt 12pt;
    text-align: left;
}

th {
    background-color: #f6f8fa;
    font-weight: 600;
}

/* Blockquotes */
blockquote {
    margin: 12pt 0;
    padding: 0 12pt;
    border-left: 4pt solid #dfe2e5;
    color: #6a737d;
    font-style: italic;
}

/* Links */
a {
    color: #0366d6;
    text-decoration: none;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 12pt auto;
}

/* Table of Contents */
.table-of-contents {
    margin-bottom: 24pt;
    padding: 12pt;
    background-color: #f8f9fa;
    border-radius: 6pt;
    border: 1pt solid #e1e4e8;
}

.table-of-contents h2 {
    margin-top: 0;
    margin-bottom: 12pt;
    font-size: 16pt;
    border-bottom: none;
    padding-bottom: 0;
}

.toc-list {
    list-style: none;
    padding-left: 0;
}

.toc-list li {
    margin: 6pt 0;
}

.toc-list a {
    color: #0366d6;
    text-decoration: none;
}

.toc-level-1 {
    font-weight: 600;
}

.toc-level-2 {
    padding-left: 12pt;
}

.toc-level-3 {
    padding-left: 24pt;
}

.toc-level-4 {
    padding-left: 36pt;
}

.toc-level-5 {
    padding-left: 48pt;
}

.toc-level-6 {
    padding-left: 60pt;
}

/* File separator */
.file-separator {
    margin: 36pt 0;
    border-top: 2pt solid #e1e4e8;
    page-break-before: auto;
}

/* Page breaks */
.page-break {
    page-break-before: always;
}

/* Print-specific styles */
@media print {
    body {
        font-size: 10pt;
    }
    
    h1 {
        font-size: 20pt;
    }
    
    h2 {
        font-size: 16pt;
    }
    
    h3 {
        font-size: 13pt;
    }
    
    h4 {
        font-size: 11pt;
    }
    
    h5, h6 {
        font-size: 10pt;
    }
}
"""


def _get_github_style() -> str:
    """GitHub-flavored styling."""
    return """
/* GitHub Style */

/* Base styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #24292f;
    background-color: #ffffff;
    max-width: none;
    margin: 0;
    padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    margin-top: 24pt;
    margin-bottom: 12pt;
    font-weight: 600;
    line-height: 1.25;
    color: #24292f;
}

h1 {
    font-size: 24pt;
    padding-bottom: 8pt;
    border-bottom: 1pt solid #d0d7de;
}

h2 {
    font-size: 18pt;
    padding-bottom: 6pt;
    border-bottom: 1pt solid #d0d7de;
}

h3 {
    font-size: 14pt;
}

h4 {
    font-size: 12pt;
}

h5 {
    font-size: 11pt;
}

h6 {
    font-size: 10pt;
    color: #656d76;
}

/* Paragraphs */
p {
    margin-top: 0;
    margin-bottom: 12pt;
}

/* Lists */
ul, ol {
    margin-top: 0;
    margin-bottom: 12pt;
    padding-left: 24pt;
}

li {
    margin: 3pt 0;
}

li > p {
    margin-top: 12pt;
}

li + li {
    margin-top: 3pt;
}

/* Code */
code, tt {
    font-family: ui-monospace, SFMono-Regular, 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
    font-size: 10pt;
    padding: 2pt 4pt;
    margin: 0;
    background-color: rgba(175, 184, 193, 0.2);
    border-radius: 6pt;
}

pre {
    font-family: ui-monospace, SFMono-Regular, 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
    font-size: 10pt;
    margin-top: 0;
    margin-bottom: 12pt;
    padding: 12pt;
    overflow: auto;
    background-color: #f6f8fa;
    border-radius: 6pt;
    border: 1pt solid #d0d7de;
}

pre code {
    background: transparent;
    border: 0;
    padding: 0;
    margin: 0;
    border-radius: 0;
}

/* Tables */
table {
    border-spacing: 0;
    border-collapse: collapse;
    margin-top: 0;
    margin-bottom: 12pt;
    width: 100%;
}

td, th {
    padding: 6pt 12pt;
    border: 1pt solid #d0d7de;
}

th {
    font-weight: 600;
    background-color: #f6f8fa;
}

tr:nth-child(2n) {
    background-color: #f6f8fa;
}

/* Blockquotes */
blockquote {
    margin: 0;
    padding: 0 12pt;
    color: #656d76;
    border-left: 3pt solid #d0d7de;
}

blockquote > :first-child {
    margin-top: 0;
}

blockquote > :last-child {
    margin-bottom: 0;
}

/* Links */
a {
    color: #0969da;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    box-sizing: content-box;
    background-color: #ffffff;
}

/* Horizontal rules */
hr {
    height: 3pt;
    padding: 0;
    margin: 18pt 0;
    background-color: #d0d7de;
    border: 0;
}

/* Table of Contents */
.table-of-contents {
    margin-bottom: 24pt;
    padding: 12pt;
    background-color: #f6f8fa;
    border: 1pt solid #d0d7de;
    border-radius: 6pt;
}

.table-of-contents h2 {
    margin-top: 0;
    margin-bottom: 12pt;
    font-size: 16pt;
    border-bottom: none;
    padding-bottom: 0;
}

.toc-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
}

.toc-list li {
    margin: 6pt 0;
}

.toc-list a {
    color: #0969da;
    text-decoration: none;
}

.toc-level-1 {
    font-weight: 600;
}

.toc-level-2 {
    padding-left: 12pt;
}

.toc-level-3 {
    padding-left: 24pt;
}

.toc-level-4 {
    padding-left: 36pt;
}

.toc-level-5 {
    padding-left: 48pt;
}

.toc-level-6 {
    padding-left: 60pt;
}

/* File separator */
.file-separator {
    margin: 36pt 0;
    border-top: 2pt solid #d0d7de;
}

/* Syntax highlighting */
.highlight {
    background: #f6f8fa;
}

.highlight .c { color: #6a737d; } /* Comment */
.highlight .k { color: #d73a49; } /* Keyword */
.highlight .s { color: #032f62; } /* String */
.highlight .n { color: #24292f; } /* Name */
.highlight .o { color: #d73a49; } /* Operator */
"""


def _get_minimal_style() -> str:
    """Minimal design with focus on content."""
    return """
/* Minimal Style */

/* Base styles */
body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #000;
    max-width: none;
    margin: 0;
    padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-weight: 400;
    line-height: 1.2;
    margin-top: 24pt;
    margin-bottom: 12pt;
    color: #000;
}

h1 {
    font-size: 24pt;
    text-align: center;
    margin-bottom: 24pt;
}

h2 {
    font-size: 18pt;
}

h3 {
    font-size: 14pt;
}

h4 {
    font-size: 12pt;
}

h5, h6 {
    font-size: 11pt;
}

/* Paragraphs */
p {
    margin: 0 0 12pt 0;
    text-align: justify;
    text-indent: 0;
}

/* Lists */
ul, ol {
    margin: 12pt 0;
    padding-left: 24pt;
}

li {
    margin: 3pt 0;
}

/* Code */
code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 10pt;
}

pre {
    font-family: 'Courier New', Courier, monospace;
    font-size: 10pt;
    margin: 12pt 0;
    padding: 12pt;
    border: 1pt solid #ccc;
    background-color: #f9f9f9;
}

/* Tables */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12pt 0;
}

th, td {
    border: 1pt solid #000;
    padding: 6pt 12pt;
    text-align: left;
}

th {
    font-weight: bold;
}

/* Blockquotes */
blockquote {
    margin: 12pt 24pt;
    padding: 0;
    font-style: italic;
}

/* Links */
a {
    color: #000;
    text-decoration: underline;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 12pt auto;
}

/* Table of Contents */
.table-of-contents {
    margin-bottom: 36pt;
    text-align: center;
}

.table-of-contents h2 {
    margin-top: 0;
    margin-bottom: 18pt;
    font-size: 16pt;
}

.toc-list {
    list-style: none;
    padding-left: 0;
    text-align: left;
    display: inline-block;
}

.toc-list li {
    margin: 6pt 0;
}

.toc-list a {
    color: #000;
    text-decoration: none;
}

.toc-level-1 {
    font-weight: bold;
}

.toc-level-2 {
    padding-left: 12pt;
}

.toc-level-3 {
    padding-left: 24pt;
}

.toc-level-4 {
    padding-left: 36pt;
}

/* File separator */
.file-separator {
    margin: 48pt 0;
    text-align: center;
}

.file-separator::after {
    content: "* * *";
    font-size: 14pt;
}

/* Page breaks */
.page-break {
    page-break-before: always;
}
"""


def _get_academic_style() -> str:
    """Professional academic paper style."""
    return """
/* Academic Style */

/* Base styles */
body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #000;
    max-width: none;
    margin: 0;
    padding: 0;
    text-align: justify;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Times New Roman', Times, serif;
    font-weight: bold;
    line-height: 1.2;
    margin-top: 18pt;
    margin-bottom: 12pt;
    color: #000;
    text-align: left;
}

h1 {
    font-size: 16pt;
    text-align: center;
    margin-top: 0;
    margin-bottom: 24pt;
    text-transform: uppercase;
    letter-spacing: 1pt;
}

h2 {
    font-size: 14pt;
    margin-top: 24pt;
}

h3 {
    font-size: 12pt;
    font-style: italic;
}

h4 {
    font-size: 11pt;
    font-weight: normal;
    font-style: italic;
}

h5, h6 {
    font-size: 11pt;
    font-weight: normal;
}

/* Paragraphs */
p {
    margin: 0 0 12pt 0;
    text-align: justify;
    text-indent: 12pt;
}

p:first-child,
h1 + p,
h2 + p,
h3 + p,
h4 + p,
h5 + p,
h6 + p {
    text-indent: 0;
}

/* Lists */
ul, ol {
    margin: 12pt 0;
    padding-left: 24pt;
}

li {
    margin: 6pt 0;
    text-align: justify;
}

/* Code */
code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 10pt;
}

pre {
    font-family: 'Courier New', Courier, monospace;
    font-size: 10pt;
    margin: 12pt 0;
    padding: 12pt;
    border: 1pt solid #000;
    background-color: #f8f8f8;
    text-align: left;
}

/* Tables */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 18pt auto;
    font-size: 10pt;
}

th, td {
    border: 1pt solid #000;
    padding: 6pt 8pt;
    text-align: center;
    vertical-align: top;
}

th {
    font-weight: bold;
    background-color: #f0f0f0;
}

caption {
    font-weight: bold;
    margin-bottom: 6pt;
    text-align: center;
}

/* Blockquotes */
blockquote {
    margin: 12pt 36pt;
    padding: 0;
    font-style: italic;
    font-size: 10pt;
}

/* Links */
a {
    color: #000;
    text-decoration: none;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 18pt auto;
}

/* Figures */
figure {
    margin: 18pt 0;
    text-align: center;
}

figcaption {
    font-size: 10pt;
    font-style: italic;
    margin-top: 6pt;
}

/* Table of Contents */
.table-of-contents {
    margin-bottom: 36pt;
    page-break-after: always;
}

.table-of-contents h2 {
    text-align: center;
    margin-top: 0;
    margin-bottom: 24pt;
    font-size: 14pt;
    text-transform: uppercase;
    letter-spacing: 1pt;
}

.toc-list {
    list-style: none;
    padding-left: 0;
}

.toc-list li {
    margin: 9pt 0;
    text-indent: 0;
}

.toc-list a {
    color: #000;
    text-decoration: none;
}

.toc-level-1 {
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
}

.toc-level-2 {
    padding-left: 12pt;
    font-weight: bold;
}

.toc-level-3 {
    padding-left: 24pt;
    font-style: italic;
}

.toc-level-4 {
    padding-left: 36pt;
}

.toc-level-5 {
    padding-left: 48pt;
}

.toc-level-6 {
    padding-left: 60pt;
}

/* File separator */
.file-separator {
    margin: 36pt 0;
    page-break-before: always;
}

/* Footnotes */
.footnote {
    font-size: 9pt;
    vertical-align: super;
}

/* Page breaks */
.page-break {
    page-break-before: always;
}

/* Abstract */
.abstract {
    margin: 24pt 36pt;
    font-size: 10pt;
    text-align: justify;
}

.abstract h3 {
    text-align: center;
    font-size: 11pt;
    margin-bottom: 12pt;
}

/* References */
.references {
    font-size: 10pt;
}

.references h2 {
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1pt;
}

/* Print-specific styles */
@media print {
    body {
        font-size: 10pt;
    }
    
    h1 {
        font-size: 14pt;
    }
    
    h2 {
        font-size: 12pt;
    }
    
    h3 {
        font-size: 11pt;
    }
    
    h4, h5, h6 {
        font-size: 10pt;
    }
}
"""




def _get_modern_style() -> str:
    """Modern contemporary design with clean typography."""
    return """
/* Modern Style - Contemporary design with modern typography */

/* Base styles */
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 11pt;
    line-height: 1.7;
    color: #1a1a1a;
    max-width: none;
    margin: 0;
    padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    line-height: 1.3;
    margin-top: 24pt;
    margin-bottom: 12pt;
    color: #0f172a;
}

h1 {
    font-size: 28pt;
    color: #1e40af;
    margin-bottom: 24pt;
}

h2 {
    font-size: 20pt;
    color: #1e3a8a;
    border-bottom: 2pt solid #e2e8f0;
    padding-bottom: 8pt;
}

h3 {
    font-size: 16pt;
    color: #334155;
}

h4 {
    font-size: 14pt;
}

h5, h6 {
    font-size: 12pt;
    color: #64748b;
}

/* Code blocks */
pre {
    background: #0f172a;
    color: #e2e8f0;
    padding: 16pt;
    border-radius: 8pt;
    border-left: 4pt solid #3b82f6;
}

/* Tables */
table {
    box-shadow: 0 1pt 3pt rgba(0, 0, 0, 0.1);
    border-radius: 8pt;
    overflow: hidden;
}

th {
    background: #f8fafc;
    color: #374151;
}
"""


def _get_dark_style() -> str:
    """Dark mode theme for reduced eye strain."""
    return """
/* Dark Style - Dark mode theme */

/* Page background */
@page {
    background-color: #0f172a;
}

/* Base styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #e2e8f0;
    background-color: #0f172a;
    max-width: none;
    margin: 0;
    padding: 0;
}

/* Headings */
h1 {
    color: #60a5fa;
    border-bottom: 2pt solid #1e293b;
}

h2 {
    color: #38bdf8;
    border-bottom: 1pt solid #1e293b;
}

h3 {
    color: #22d3ee;
}

h4 {
    color: #a78bfa;
}

h5, h6 {
    color: #94a3b8;
}

/* Code */
code {
    background-color: #1e293b;
    color: #06b6d4;
    border: 1pt solid #334155;
}

pre {
    background-color: #1e293b;
    color: #e2e8f0;
    border: 1pt solid #334155;
}

/* Tables */
table {
    background-color: #1e293b;
}

th {
    background-color: #334155;
    color: #f1f5f9;
}

th, td {
    border: 1pt solid #334155;
}

/* Blockquotes */
blockquote {
    margin: 12pt 0;
    padding: 0 12pt;
    border-left: 4pt solid #3b82f6;
    color: #94a3b8;
    font-style: italic;
    background-color: #1e293b;
}

/* Links */
a {
    color: #60a5fa;
    text-decoration: none;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 12pt auto;
    border-radius: 6pt;
    border: 1pt solid #334155;
}

/* Lists */
ul, ol {
    margin: 12pt 0;
    padding-left: 24pt;
}

li {
    margin: 6pt 0;
    color: #e2e8f0;
}

/* Paragraphs */
p {
    margin: 0 0 12pt 0;
    text-align: justify;
    color: #e2e8f0;
}

/* All headings base styles */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.3;
    margin-top: 24pt;
    margin-bottom: 12pt;
}
"""


def _get_technical_style() -> str:
    """Technical documentation with monospaced fonts."""
    return """
/* Technical Style - Monospaced technical documentation */

/* Base styles */
body {
    font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Monaco, monospace;
    font-size: 10pt;
    line-height: 1.5;
    color: #1a1a1a;
    background-color: #fafafa;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: inherit;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1pt;
}

h1 {
    font-size: 16pt;
    border: 2pt solid #000;
    padding: 8pt;
    text-align: center;
    background-color: #000;
    color: #fff;
}

h2 {
    font-size: 14pt;
    border-bottom: 1pt solid #000;
}

h3 {
    font-size: 12pt;
    text-decoration: underline;
}

/* Code maintains same font */
code, pre {
    font-family: inherit;
    background-color: #f0f0f0;
    border: 1pt solid #000;
}

/* Tables */
table {
    border-collapse: collapse;
    font-size: 9pt;
}

th, td {
    border: 1pt solid #000;
    padding: 4pt 6pt;
}

th {
    background-color: #e0e0e0;
}
"""


def _get_book_style() -> str:
    """Classic book typography with elegant serif fonts."""
    return """
/* Book Style - Classic book typography */

/* Base styles */
body {
    font-family: 'Crimson Text', 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #2c2c2c;
    text-align: justify;
    hyphens: auto;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', 'Georgia', serif;
    color: #1a1a1a;
}

h1 {
    font-size: 24pt;
    text-align: center;
    font-weight: 700;
    letter-spacing: 2pt;
    text-transform: uppercase;
    margin-bottom: 36pt;
}

h2 {
    font-size: 18pt;
    font-weight: 600;
    font-style: italic;
}

h3 {
    font-size: 14pt;
    font-weight: 600;
}

/* Paragraphs with indentation */
p {
    text-indent: 18pt;
    margin-bottom: 12pt;
}

p:first-child,
h1 + p,
h2 + p,
h3 + p {
    text-indent: 0;
}

/* Elegant blockquotes */
blockquote {
    margin: 18pt 36pt;
    font-style: italic;
    text-align: center;
    font-size: 10pt;
}

/* Links with dotted underline */
a {
    color: #1a1a1a;
    text-decoration: none;
    border-bottom: 1pt dotted #666;
}
"""


def _get_presentation_style() -> str:
    """Large fonts optimized for presentations."""
    return """
/* Presentation Style - Large fonts for presentations */

/* Base styles */
body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 16pt;
    line-height: 1.4;
    color: #1a1a1a;
    padding: 24pt;
}

/* Large headings */
h1 {
    font-size: 48pt;
    font-weight: 100;
    text-align: center;
    color: #2563eb;
    text-transform: uppercase;
    letter-spacing: 3pt;
    margin-bottom: 48pt;
}

h2 {
    font-size: 36pt;
    font-weight: 200;
    color: #1e40af;
    border-bottom: 3pt solid #3b82f6;
    padding-bottom: 12pt;
}

h3 {
    font-size: 28pt;
    color: #1e3a8a;
}

h4 {
    font-size: 22pt;
}

h5, h6 {
    font-size: 18pt;
}

/* Large text and spacing */
p {
    font-size: 16pt;
    line-height: 1.5;
    margin-bottom: 24pt;
}

ul, ol {
    font-size: 16pt;
    margin: 24pt 0;
    padding-left: 36pt;
}

li {
    margin: 12pt 0;
}

/* Prominent code blocks */
pre {
    font-size: 14pt;
    background-color: #1e293b;
    color: #e2e8f0;
    padding: 24pt;
    border-radius: 12pt;
    margin: 36pt 0;
}

/* Large tables */
table {
    font-size: 14pt;
    margin: 36pt 0;
}

th {
    font-size: 16pt;
    padding: 12pt 18pt;
}

/* Emphasized blockquotes */
blockquote {
    font-size: 18pt;
    margin: 36pt 48pt;
    padding: 24pt;
    border-left: 6pt solid #3b82f6;
    background-color: #f8fafc;
    border-radius: 0 12pt 12pt 0;
}

/* Presentation emphasis */
strong {
    font-weight: 700;
    color: #dc2626;
    font-size: 120%;
}

em {
    color: #7c3aed;
}
"""
