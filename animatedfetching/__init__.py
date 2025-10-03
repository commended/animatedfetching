"""
AnimatedFetching - A terminal fetch program with animated GIF support
"""

__version__ = "1.0.0"

from .main import main, AnimatedFetching
from .config import Config
from .sysinfo import SystemInfo
from .animation import AnimatedGIF

__all__ = ['main', 'AnimatedFetching', 'Config', 'SystemInfo', 'AnimatedGIF']
