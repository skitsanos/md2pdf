# Getting Started with md2pdf

Welcome to **md2pdf**, a powerful Markdown to PDF converter!

## What is md2pdf?

md2pdf is a CLI tool that converts Markdown documents into beautiful PDFs with customizable styling.

### Key Features

- **13+ Built-in Styles:** From GitHub to Academic to Corporate themes
- **YAML-based Custom Themes:** Easy creation of your own styles  
- **Docker Support:** Containerized usage without dependencies
- **Table of Contents:** Automatic generation with proper linking
- **File Merging:** Combine multiple Markdown files into one PDF

## Quick Start

### Installation

```bash
git clone https://github.com/skitsanos/md2pdf.git
cd md2pdf
pip install -e .
```

### Basic Usage

```bash
# Convert with default style
md2pdf document.md -o output.pdf

# Use purple light theme
md2pdf document.md -o styled.pdf --style purple-light

# Generate with table of contents
md2pdf document.md -o complete.pdf --style purple-dark --toc
```

### Docker Usage

```bash
# Build and run with Docker
docker build -t md2pdf .
docker run --rm -v "$(pwd):/docs" md2pdf document.md -o output.pdf --style purple-light
```

## Available Styles

| Style | Type | Description |
|-------|------|-------------|
| `purple-light` | YAML | Elegant purple theme with Montserrat font |
| `purple-dark` | YAML | Dark mystique with purple accents |
| `github` | Built-in | GitHub-flavored styling |
| `academic` | Built-in | Professional academic format |
| `ibm` | YAML | Corporate IBM Carbon Design |

## Code Example

Here's how to use md2pdf programmatically:

```python
from pathlib import Path
from md2pdf.converter import MarkdownToPDFConverter

# Create converter instance
converter = MarkdownToPDFConverter(verbose=True)

# Convert files
converter.convert_files_to_pdf(
    input_files=[Path("example.md")],
    output_path=Path("output.pdf"),
    style="purple-light",
    generate_toc=True,
    title="My Document"
)
```

## Next Steps

1. **Explore Themes:** Try different built-in and YAML styles
2. **Create Custom Styles:** Use the YAML template to build your own themes
3. **Batch Processing:** Convert multiple files at once
4. **Docker Deployment:** Use containerized version for production

> **Tip:** Check out the `samples/showcase.md` file for a comprehensive demonstration of all features!

---

*Start converting your Markdown documents to beautiful PDFs today!* ✨