# md2pdf Style Showcase

This document demonstrates the **md2pdf** CLI tool's capabilities across different styling themes and markdown features.

## Typography and Headings

### Level 3 Heading
#### Level 4 Heading
##### Level 5 Heading
###### Level 6 Heading

This paragraph demonstrates **bold text**, *italic text*, and `inline code` formatting. You can also combine formatting like ***bold italic*** text.

## Code Examples

Here's a Python code block with syntax highlighting:

```python
def convert_markdown_to_pdf(input_file, output_file, style="default"):
    """
    Convert a Markdown file to PDF using md2pdf.
    
    Args:
        input_file (str): Path to the input Markdown file
        output_file (str): Path for the output PDF file  
        style (str): Style theme to apply
    """
    from md2pdf import MarkdownToPDFConverter
    
    converter = MarkdownToPDFConverter(verbose=True)
    converter.convert_files_to_pdf(
        input_files=[Path(input_file)],
        output_path=Path(output_file),
        style=style,
        generate_toc=True
    )
    
    print(f"✓ PDF created successfully: {output_file}")
```

JavaScript example:

```javascript
// Modern async/await function
async function fetchMarkdownContent(url) {
    try {
        const response = await fetch(url);
        const markdown = await response.text();
        
        return {
            success: true,
            content: markdown,
            timestamp: new Date().toISOString()
        };
    } catch (error) {
        console.error('Failed to fetch markdown:', error);
        return { success: false, error: error.message };
    }
}
```

## Lists and Organization

### Unordered Lists

- **Built-in Styles:**
  - GitHub-flavored styling
  - Academic paper format
  - Minimal clean design
  - Corporate IBM theme
  - Modern typography
  - Dark mode support

- **YAML-based Themes:**
  - Cyberpunk futuristic
  - Nature earth-tones
  - Ocean blue gradients
  - Retro synthwave
  - Purple light elegance
  - Purple dark mystique

### Ordered Lists

1. **Installation Process:**
   1. Clone the repository
   2. Install dependencies
   3. Run the setup script

2. **Usage Workflow:**
   1. Prepare Markdown files
   2. Choose a style theme
   3. Execute conversion command
   4. Review generated PDF

3. **Docker Deployment:**
   1. Build the Docker image
   2. Mount input/output volumes
   3. Run conversion in container

## Tables and Data

| Style Name | Type | Font Family | Use Case |
|------------|------|-------------|----------|
| `github` | Built-in | System fonts | Documentation |
| `academic` | Built-in | Serif fonts | Research papers |
| `ibm` | YAML | IBM Plex | Corporate reports |
| `purple-light` | YAML | Montserrat | Creative presentations |
| `purple-dark` | YAML | Montserrat | Dark mode documents |

### Feature Comparison

| Feature | CLI | Docker | YAML Styles | Built-in Styles |
|---------|-----|--------|-------------|-----------------|
| Single file conversion | ✅ | ✅ | ✅ | ✅ |
| Multiple file merging | ✅ | ✅ | ✅ | ✅ |
| Table of contents | ✅ | ✅ | ✅ | ✅ |
| Custom CSS | ✅ | ✅ | N/A | N/A |
| Variable substitution | N/A | N/A | ✅ | N/A |
| Easy distribution | ✅ | ✅ | ✅ | ✅ |

## Blockquotes and Callouts

> **Note:** This is a standard blockquote that can contain multiple paragraphs and other formatting.
>
> It supports **bold**, *italic*, and `code` formatting within the quote block.

> **Important:** When using Docker, make sure to properly mount your input and output directories:
> 
> ```bash
> docker run --rm -v "$(pwd):/docs" md2pdf document.md -o output.pdf --style purple-light
> ```

## Mathematical and Special Content

While md2pdf doesn't support LaTeX math rendering by default, you can include mathematical concepts in text:

- Variables: x, y, z
- Functions: f(x) = ax² + bx + c
- Sets: A ∪ B, A ∩ B
- Greek letters: α, β, γ, δ, π, σ, λ

## Links and References

- **Official Repository:** [github.com/skitsanos/md2pdf](https://github.com/skitsanos/md2pdf)
- **Docker Hub:** Coming soon for easy distribution
- **Documentation:** Comprehensive README with examples
- **License:** MIT License for open source usage

## Command Examples

### Basic Usage
```bash
# Convert single file with default style
md2pdf document.md -o output.pdf

# Convert with GitHub styling
md2pdf README.md -o readme.pdf --style github

# Use purple themes
md2pdf presentation.md -o slides.pdf --style purple-light
md2pdf report.md -o dark-report.pdf --style purple-dark
```

### Advanced Features
```bash
# Generate table of contents
md2pdf manual.md -o manual.pdf --toc --style academic

# Multiple files with custom title
md2pdf intro.md guide.md api.md -o complete.pdf --title "Complete Guide" --style ibm

# Docker usage
docker run --rm -v "$(pwd):/docs" md2pdf *.md -o all-docs.pdf --style purple-dark --toc
```

## Styling Features Showcase

### Typography Hierarchy

The purple themes feature elegant **Montserrat** typography for readability and professional appearance. Code blocks use **Monaco** for clear monospace formatting.

### Color Schemes

- **Purple Light:** Elegant purple gradients on white background
- **Purple Dark:** Mystical dark theme with purple accents and subtle glows

### Interactive Elements

Links are styled with hover effects and smooth transitions. Tables include alternating row colors for better readability.

---

## Conclusion

The **md2pdf** tool provides a comprehensive solution for converting Markdown documents to professional PDFs. With support for:

1. **Multiple styling options** (13+ built-in styles + YAML themes)
2. **Docker containerization** for easy deployment
3. **Advanced features** like table of contents and file merging
4. **Custom typography** with web fonts support
5. **Security validation** and error handling

Whether you're creating documentation, reports, presentations, or academic papers, md2pdf offers the flexibility and quality you need.

### Try It Out

```bash
# Install md2pdf
git clone https://github.com/skitsanos/md2pdf.git
cd md2pdf
pip install -e .

# Convert this showcase document
md2pdf samples/showcase.md -o showcase-purple-light.pdf --style purple-light --toc
md2pdf samples/showcase.md -o showcase-purple-dark.pdf --style purple-dark --toc
```

*Happy document converting! 🎨📄*