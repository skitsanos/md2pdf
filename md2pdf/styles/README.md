# YAML Styles for md2pdf

This directory contains YAML-based style definitions that can be used with md2pdf. YAML styles offer a more flexible and maintainable way to define PDF styles compared to writing raw CSS.

## Creating Your Own Style

1. Copy `template.yaml` to a new file (e.g., `mystyle.yaml`)
2. Edit the metadata, variables, and selectors
3. Use your style with: `md2pdf input.md --output output.pdf --style mystyle`

## Style Structure

### Metadata
```yaml
meta:
  name: "Style Name"
  description: "Brief description"
  author: "Your Name"
  version: "1.0"
```

### Variables
Define reusable values:
```yaml
variables:
  primary_color: "#333333"
  font_family: "'Arial', sans-serif"
  font_size: "11pt"
```

Use variables in selectors with `${variable_name}` syntax.

### Selectors (Dictionary Mode)
Define CSS rules using camelCase property names:
```yaml
selectors:
  body:
    fontFamily: "${font_family}"
    fontSize: "${font_size}"
    color: "${primary_color}"
  
  h1:
    fontSize: "24pt"
    textAlign: "center"
```

### Template Mode
For complex styles, use Jinja2 templates:
```yaml
template: |
  /* Custom CSS */
  body {
      font-family: {{ variables.font_family }};
      color: {{ variables.primary_color }};
  }
  
  h1 {
      font-size: 24pt;
      color: {{ variables.accent_color }};
  }
```

## Property Name Conversion

YAML property names in camelCase are automatically converted to CSS kebab-case:
- `fontFamily` → `font-family`
- `backgroundColor` → `background-color`
- `marginTop` → `margin-top`

## Example Styles

- **cyberpunk.yaml** - Futuristic neon green/magenta theme
- **nature.yaml** - Earth-toned nature-inspired theme  
- **retro.yaml** - 1980s synthwave style with gradients
- **template.yaml** - Basic template for creating new styles

## Tips

1. Use the `page` selector to set page-level properties like background color
2. Define commonly used values as variables for consistency
3. Test your styles with sample documents
4. Use descriptive color names in your variables
5. Consider print-specific requirements (avoid pure black/white for better printing)

## Troubleshooting

- **Style not found**: Make sure the YAML file is in the styles directory
- **Invalid YAML**: Check syntax with a YAML validator
- **CSS not rendering**: Verify property names and values are valid CSS
- **Colors not working**: Use hex codes, RGB, or valid CSS color names