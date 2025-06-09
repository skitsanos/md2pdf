#!/usr/bin/env python3
"""
Setup script for md2pdf CLI tool.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() if (this_directory / "README.md").exists() else ""

setup(
    name="md2pdf",
    version="1.0.0",
    author="skitsanos",
    author_email="",
    description="Convert Markdown documents to PDF with customizable CSS styling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skitsanos/md2pdf",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'md2pdf': ['templates/*.html', 'styles/*.yaml', 'styles/*.md'],
    },
    install_requires=[
        "click>=8.0.0",
        "markdown>=3.4.0",
        "weasyprint>=56.0",
        "pathlib2>=2.3.0",
        "Pygments>=2.10.0",
        "jinja2>=3.0.0",
        "beautifulsoup4>=4.10.0",
        "PyYAML>=6.0",
    ],
    entry_points={
        'console_scripts': [
            'md2pdf=md2pdf.cli:main',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    keywords="markdown pdf converter cli documentation",
)

