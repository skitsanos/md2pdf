#!/usr/bin/env python3
"""
Standalone script to run md2pdf tool.
"""

import sys
from pathlib import Path

# Add the project root to Python path to find md2pdf package
sys.path.insert(0, str(Path(__file__).parent))

from md2pdf.cli import main

if __name__ == '__main__':
    main()
