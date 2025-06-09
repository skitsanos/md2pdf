# md2pdf - Markdown to PDF CLI Tool

A powerful Python CLI tool that converts one or more Markdown documents into a single PDF file with customizable CSS styling.

## Features

- ✅ Convert single or multiple Markdown files to PDF
- ✅ Support for glob patterns (e.g., `*.md`, `docs/*.md`)
- ✅ 13+ built-in styles including corporate, dark mode, and themed options
- ✅ YAML-based style system for easy customization
- ✅ Custom CSS file support
- ✅ Table of contents generation
- ✅ Customizable page margins and sizes
- ✅ File merging capabilities
- ✅ Comprehensive error handling and validation
- ✅ Security features (input sanitization, path validation)
- ✅ Production-ready logging system
- ✅ Cross-platform compatibility
- ✅ Docker support for containerized usage

## Installation

### From Source

```bash
git clone https://github.com/skitsanos/md2pdf.git
cd md2pdf
pip install -e .
```

### Using Docker

```bash
# Build the Docker image
git clone https://github.com/skitsanos/md2pdf.git
cd md2pdf
docker build -t md2pdf .

# Or pull from Docker Hub (when published)
docker pull skitsanos/md2pdf
```

### Using pip (when published)

```bash
pip install md2pdf
```

## Requirements

- Python 3.7 or higher
- Dependencies (automatically installed):
  - click>=8.0.0
  - markdown>=3.4.0
  - weasyprint>=56.0
  - jinja2>=3.0.0
  - beautifulsoup4>=4.10.0
  - Pygments>=2.10.0
  - PyYAML>=6.0

## Usage

### Basic Usage

```bash
# Convert single file
md2pdf document.md --output report.pdf

# Convert multiple files
md2pdf intro.md chapter1.md chapter2.md --output book.pdf

# Use glob patterns
md2pdf docs/*.md --output documentation.pdf
```

### Styling Options

```bash
# Use built-in styles
md2pdf README.md --output readme.pdf --style github
md2pdf paper.md --output paper.pdf --style academic
md2pdf notes.md --output notes.pdf --style minimal
md2pdf report.md --output report.pdf --style ibm

# YAML-based themes
md2pdf document.md --output doc.pdf --style cyberpunk
md2pdf report.md --output report.pdf --style nature
md2pdf slides.md --output slides.pdf --style retro

# Use custom CSS
md2pdf document.md --output styled.pdf --style custom.css
```

### Advanced Features

```bash
# Generate table of contents
md2pdf manual.md --output manual.pdf --toc --style academic

# Custom title and margins
md2pdf docs/*.md --output manual.pdf --title "User Manual" --margin 15mm

# Different page sizes
md2pdf report.md --output report.pdf --page-size Letter

# Verbose output for debugging
md2pdf document.md --output output.pdf --verbose
```

### Docker Usage

```bash
# Convert single file (mount current directory)
docker run --rm -v "$(pwd):/docs" md2pdf document.md -o report.pdf

# Convert with specific style
docker run --rm -v "$(pwd):/docs" md2pdf README.md -o readme.pdf --style github

# Convert multiple files with table of contents
docker run --rm -v "$(pwd):/docs" md2pdf docs/*.md -o manual.pdf --toc --style academic

# Convert with custom CSS (mount CSS file directory)
docker run --rm -v "$(pwd):/docs" -v "/path/to/css:/css" md2pdf document.md -o styled.pdf --style /css/custom.css

# Interactive mode for multiple operations
docker run -it --rm -v "$(pwd):/docs" md2pdf /bin/bash
```

### Command Line Options

- `INPUT_FILES`: One or more Markdown files or glob patterns (required)
- `--output`, `-o`: Output PDF file path (required)
- `--style`, `-s`: CSS styling (see Built-in Styles below, or path to CSS file)
- `--title`: Set PDF document title (defaults to first heading or filename)
- `--margin`: Set page margins (e.g., "20mm", "1in"). Default: 20mm
- `--page-size`: Specify page size (A4, Letter, Legal, etc.). Default: A4
- `--toc/--no-toc`: Generate table of contents. Default: disabled
- `--merge/--no-merge`: Merge multiple files into single document. Default: enabled
- `--verbose`, `-v`: Enable verbose output for debugging

## Built-in Styles

### Python-based Styles
- **default** - Clean, readable style with good typography
- **github** - GitHub-flavored styling with familiar appearance
- **minimal** - Minimal design with focus on content
- **academic** - Professional academic paper style
- **modern** - Contemporary design with modern typography
- **dark** - Dark mode theme for reduced eye strain
- **technical** - Technical documentation with monospaced fonts
- **book** - Classic book typography with elegant serif fonts
- **presentation** - Large fonts optimized for presentations

### YAML-based Themes
- **ibm** - Corporate IBM Carbon Design System inspired theme
- **cyberpunk** - Futuristic cyberpunk theme with neon colors
- **nature** - Earth-toned theme inspired by nature
- **ocean** - Calming ocean-themed style with blue gradients
- **retro** - 1980s retro style with synthwave colors

## Creating Custom YAML Styles

You can create your own styles using YAML files in the `styles/` directory:

1. Copy `styles/template.yaml` to create a new style
2. Customize colors, fonts, and layout properties
3. Use variables for consistency across your theme
4. Apply with `--style your-style-name`

Example YAML style structure:
```yaml
meta:
  name: "My Style"
  description: "Custom theme"

variables:
  primary_color: "#0066cc"
  font_family: "'Arial', sans-serif"

selectors:
  body:
    fontFamily: "${font_family}"
    color: "${primary_color}"
```

See `styles/README.md` for detailed documentation.

## Examples

### Convert README with GitHub styling
```bash
md2pdf README.md --output readme.pdf --style github
```

### Create corporate report with IBM styling
```bash
md2pdf report.md --output report.pdf --style ibm --title "Q4 Report"
```

### Create academic paper with table of contents
```bash
md2pdf paper.md --output paper.pdf --style academic --toc --title "Research Paper"
```

### Merge multiple documentation files
```bash
md2pdf docs/intro.md docs/guide.md docs/api.md --output complete-docs.pdf --toc
```

### Use custom CSS styling
```bash
md2pdf document.md --output styled-doc.pdf --style company-style.css
```

### Docker Examples

```bash
# Corporate report with Docker
docker run --rm -v "$(pwd):/docs" md2pdf report.md -o report.pdf --style ibm --title "Q4 Report"

# Academic paper with TOC using Docker
docker run --rm -v "$(pwd):/docs" md2pdf paper.md -o paper.pdf --style academic --toc

# Multiple documentation files
docker run --rm -v "$(pwd):/docs" md2pdf docs/*.md -o complete-docs.pdf --toc --style github
```

## Supported Markdown Features

- Headers (H1-H6) with automatic anchor generation
- Text formatting (bold, italic, code)
- Lists (ordered and unordered, nested)
- Code blocks with syntax highlighting (Pygments)
- Tables with styling support
- Blockquotes
- Links (with proper handling)
- Images (with size constraints)
- Horizontal rules
- All markdown.extensions.extra features

## Task Runner Support

The project includes a Taskfile for common operations:

```bash
# Create virtual environment
task venv

# Install dependencies
task install

# Convert with specific style (example)
task basic SOURCE="document.md" OUTPUT="output.pdf"
```

## Error Handling

The tool provides comprehensive error handling for:
- Missing or unreadable input files
- Invalid output paths
- Malformed Markdown
- CSS syntax errors
- Permission issues
- Security validation (path traversal, etc.)
- PDF generation failures

## Security Features

- Input sanitization and validation
- Path traversal protection
- CSS file security checks
- HTML content sanitization
- Proper error boundaries

## Development

### Project Structure

```
md2pdf/
├── __init__.py              # Package initialization
├── __main__.py              # Module entry point
├── cli.py                   # CLI interface and argument parsing
├── converter.py             # Core conversion logic
├── styles.py                # Built-in CSS styles
├── yaml_styles.py           # YAML style system
├── utils.py                 # Helper functions
├── validators.py            # Input validation and security
├── exceptions.py            # Custom exception classes
├── constants.py             # Application constants
├── logger.py                # Logging configuration
├── templates/               # HTML templates
│   └── base.html
├── styles/                  # YAML style definitions
│   ├── README.md
│   ├── template.yaml
│   ├── ibm.yaml
│   ├── cyberpunk.yaml
│   ├── nature.yaml
│   ├── ocean.yaml
│   └── retro.yaml
├── requirements.txt         # Dependencies
└── setup.py                # Package setup
```

### Running Tests

```bash
# Test basic conversion
md2pdf test.md -o test.pdf

# Test with different styles
md2pdf test.md -o test.pdf --style github
md2pdf test.md -o test.pdf --style ibm
md2pdf test.md -o test.pdf --style cyberpunk

# Test table of contents
md2pdf test.md -o test.pdf --toc
```

## License

MIT License

Copyright (c) 2024 skitsanos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Support

For issues and questions:
- Create an issue on [GitHub](https://github.com/skitsanos/md2pdf)
- Check the documentation in `styles/README.md`
- Use `--verbose` flag for debugging output