"""
YAML-based style system for md2pdf.
"""

import yaml
from pathlib import Path
from typing import Dict, Optional, Any
from jinja2 import Template
from .exceptions import StyleError
from .logger import setup_logger


class YAMLStyleLoader:
    """Loads and processes YAML-based styles."""
    
    def __init__(self, styles_dir: Optional[Path] = None):
        """
        Initialize the YAML style loader.
        
        Args:
            styles_dir: Directory containing YAML style files
        """
        self.logger = setup_logger('md2pdf.yaml_styles')
        self.styles_dir = styles_dir or (Path(__file__).parent / "styles")
        self._style_cache: Dict[str, str] = {}
        
    def list_yaml_styles(self) -> Dict[str, str]:
        """
        List all available YAML styles.
        
        Returns:
            Dictionary mapping style names to descriptions
        """
        styles = {}
        
        if not self.styles_dir.exists():
            return styles
            
        for yaml_file in self.styles_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    style_data = yaml.safe_load(f)
                    
                if isinstance(style_data, dict) and 'meta' in style_data:
                    name = yaml_file.stem
                    description = style_data['meta'].get('description', f'Style from {yaml_file.name}')
                    styles[name] = description
                    
            except Exception as e:
                self.logger.warning(f"Failed to load style metadata from {yaml_file}: {e}")
                
        return styles
    
    def load_yaml_style(self, style_name: str) -> str:
        """
        Load a YAML style and convert it to CSS.
        
        Args:
            style_name: Name of the style (without .yaml extension)
            
        Returns:
            CSS content as string
            
        Raises:
            StyleError: If style cannot be loaded or processed
        """
        # Check cache first
        if style_name in self._style_cache:
            return self._style_cache[style_name]
            
        yaml_file = self.styles_dir / f"{style_name}.yaml"
        
        if not yaml_file.exists():
            raise StyleError(f"YAML style file not found: {yaml_file}")
            
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                style_data = yaml.safe_load(f)
                
            css_content = self._yaml_to_css(style_data, style_name)
            
            # Cache the result
            self._style_cache[style_name] = css_content
            
            self.logger.debug(f"Loaded YAML style: {style_name}")
            return css_content
            
        except Exception as e:
            raise StyleError(f"Failed to load YAML style '{style_name}': {e}")
    
    def _yaml_to_css(self, style_data: Dict[str, Any], style_name: str) -> str:
        """
        Convert YAML style definition to CSS.
        
        Args:
            style_data: Parsed YAML data
            style_name: Name of the style
            
        Returns:
            CSS content as string
        """
        if not isinstance(style_data, dict):
            raise StyleError(f"Invalid YAML format in style '{style_name}': expected dictionary")
            
        # Extract metadata
        meta = style_data.get('meta', {})
        css_template = style_data.get('template', '')
        variables = style_data.get('variables', {})
        selectors = style_data.get('selectors', {})
        
        # If there's a template, use Jinja2 to render it
        if css_template:
            template = Template(css_template)
            return template.render(
                variables=variables,
                selectors=selectors,
                meta=meta,
                style_name=style_name
            )
        
        # Otherwise, build CSS from selectors
        css_parts = [f"/* {meta.get('description', style_name)} */\n"]
        
        # Add page rules if specified
        if 'page' in selectors:
            page_rules = self._dict_to_css_rules(selectors['page'], variables)
            css_parts.append(f"@page {{\n{page_rules}\n}}\n")
            
            # Also add html/body background as fallback for better compatibility
            if 'backgroundColor' in selectors['page']:
                bg_color = selectors['page']['backgroundColor']
                # Substitute variables in background color
                for var_name, var_value in variables.items():
                    bg_color = bg_color.replace(f"${{{var_name}}}", str(var_value))
                css_parts.append(f"html, body {{\n    background-color: {bg_color};\n}}\n")
        
        # Process other selectors
        for selector, rules in selectors.items():
            if selector == 'page':
                continue  # Already handled above
                
            if isinstance(rules, dict):
                css_rules = self._dict_to_css_rules(rules, variables)
                css_parts.append(f"{selector} {{\n{css_rules}\n}}\n")
        
        return '\n'.join(css_parts)
    
    def _dict_to_css_rules(self, rules: Dict[str, Any], variables: Dict[str, str] = None) -> str:
        """
        Convert a dictionary of CSS rules to CSS text.
        
        Args:
            rules: Dictionary of CSS property-value pairs
            variables: Dictionary of variables for substitution
            
        Returns:
            CSS rules as string
        """
        if variables is None:
            variables = {}
            
        css_lines = []
        
        for property_name, value in rules.items():
            # Convert camelCase to kebab-case
            css_property = self._camel_to_kebab(property_name)
            
            # Substitute variables
            css_value = str(value)
            for var_name, var_value in variables.items():
                css_value = css_value.replace(f"${{{var_name}}}", str(var_value))
                
            css_lines.append(f"    {css_property}: {css_value};")
            
        return '\n'.join(css_lines)
    
    @staticmethod
    def _camel_to_kebab(camel_str: str) -> str:
        """Convert camelCase to kebab-case."""
        import re
        return re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', camel_str).lower()


# Global YAML style loader instance
yaml_style_loader = YAMLStyleLoader()