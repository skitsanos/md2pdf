"""
Logging configuration for md2pdf.
"""

import logging
import sys
from typing import Optional


def setup_logger(name: str = 'md2pdf', verbose: bool = False) -> logging.Logger:
    """
    Set up and configure logger for md2pdf.
    
    Args:
        name: Logger name
        verbose: Whether to enable verbose (DEBUG) logging
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Set log level
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)
    
    # Create console handler
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(level)
    
    # Create formatter
    if verbose:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
    else:
        formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


class LoggerMixin:
    """Mixin class to provide logging capabilities to other classes."""
    
    def __init__(self, *args, verbose: bool = False, **kwargs):
        """Initialize logger for the class."""
        super().__init__(*args, **kwargs)
        self.logger = setup_logger(
            name=f'md2pdf.{self.__class__.__name__}',
            verbose=verbose
        )
        self.verbose = verbose