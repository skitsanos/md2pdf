# Sample Documents

This folder contains example Markdown documents to showcase md2pdf's capabilities and styling options.

## Available Samples

### 📄 `showcase.md`
A comprehensive demonstration document featuring:
- All heading levels (H1-H6)
- Code blocks with syntax highlighting (Python, JavaScript)
- Tables with complex data
- Lists (ordered and unordered)
- Blockquotes and callouts
- Links and references
- Command examples
- Typography samples

**Recommended for:** Testing new themes and demonstrating full feature set.

### 📄 `simple-example.md`
A concise getting-started document including:
- Basic markdown formatting
- Installation instructions
- Usage examples
- Quick reference table
- Code snippets

**Recommended for:** Quick testing and documentation examples.

## Testing the Purple Themes

Try the new purple themes with these samples:

### Purple Light Theme
```bash
# Elegant light theme with purple headings
md2pdf samples/showcase.md -o showcase-purple-light.pdf --style purple-light --toc
md2pdf samples/simple-example.md -o example-purple-light.pdf --style purple-light
```

### Purple Dark Theme  
```bash
# Mystical dark theme with purple accents
md2pdf samples/showcase.md -o showcase-purple-dark.pdf --style purple-dark --toc
md2pdf samples/simple-example.md -o example-purple-dark.pdf --style purple-dark
```

## Docker Usage

Test with Docker for containerized conversion:

```bash
# Purple light theme
docker run --rm -v "$(pwd):/docs" md2pdf samples/showcase.md -o showcase-docker.pdf --style purple-light --toc

# Purple dark theme  
docker run --rm -v "$(pwd):/docs" md2pdf samples/simple-example.md -o example-docker.pdf --style purple-dark
```

## Comparing Styles

Generate the same document with different themes to compare:

```bash
# Built-in themes
md2pdf samples/showcase.md -o showcase-github.pdf --style github --toc
md2pdf samples/showcase.md -o showcase-academic.pdf --style academic --toc
md2pdf samples/showcase.md -o showcase-ibm.pdf --style ibm --toc

# YAML themes
md2pdf samples/showcase.md -o showcase-cyberpunk.pdf --style cyberpunk --toc
md2pdf samples/showcase.md -o showcase-nature.pdf --style nature --toc
md2pdf samples/showcase.md -o showcase-purple-light.pdf --style purple-light --toc
md2pdf samples/showcase.md -o showcase-purple-dark.pdf --style purple-dark --toc
```

## Font Features

The purple themes showcase **Montserrat** and **Monaco** fonts:

- **Montserrat:** Modern geometric sans-serif for body text and headings
- **Monaco:** Crisp monospace font for code blocks and inline code

These fonts provide excellent readability and professional appearance in both light and dark themes.

## Creating Your Own Samples

Use these documents as templates for your own content:

1. **Copy a sample file** as your starting point
2. **Replace content** with your own text
3. **Test with different styles** to find your preference
4. **Generate final PDF** with your chosen theme

## Tips for Best Results

- **Use semantic headings** (H1 for main title, H2 for sections, etc.)
- **Include code blocks** to test syntax highlighting
- **Add tables** to verify formatting and spacing
- **Test with --toc flag** to ensure proper heading structure
- **Try both light and dark themes** for different use cases

---

Happy document creation! 🎨📝