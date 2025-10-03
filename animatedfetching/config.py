#!/usr/bin/env python3
"""
Configuration module for AnimatedFetching
"""

import os
import json
from pathlib import Path
from jsoncomment import JsonComment

class Config:
    """Handles configuration loading from JSONC files"""
    
    DEFAULT_CONFIG_PATH = os.path.expanduser("~/.config/animatedfetching/config.jsonc")
    
    DEFAULT_CONFIG = {
        "animation": {
            "enabled": True,
            "path": "~/.config/animatedfetching/animation.gif",
            "width": 40,
            "fps": 10
        },
        "info_sections": [
            {"label": "OS", "key": "os", "color": "cyan"},
            {"label": "Kernel", "key": "kernel", "color": "blue"},
            {"label": "Uptime", "key": "uptime", "color": "green"},
            {"label": "Shell", "key": "shell", "color": "yellow"},
            {"label": "Terminal", "key": "terminal", "color": "magenta"},
            {"label": "CPU", "key": "cpu", "color": "red"},
            {"label": "Memory", "key": "memory", "color": "cyan"},
            {"label": "Disk", "key": "disk", "color": "blue"}
        ],
        "buttons": [
            {
                "label": "System Update",
                "command": "sudo apt update && sudo apt upgrade",
                "key": "u",
                "color": "green"
            },
            {
                "label": "Neofetch",
                "command": "neofetch",
                "key": "n",
                "color": "cyan"
            },
            {
                "label": "Disk Usage",
                "command": "df -h",
                "key": "d",
                "color": "yellow"
            },
            {
                "label": "Top Processes",
                "command": "top",
                "key": "t",
                "color": "red"
            }
        ],
        "layout": {
            "title": "System Information",
            "show_hostname": True,
            "separator": "─",
            "padding": 2
        },
        "colors": {
            "title": "bold cyan",
            "label": "bold",
            "separator": "dim"
        }
    }
    
    @classmethod
    def load(cls, config_path=None):
        """Load configuration from file or use defaults"""
        if config_path is None:
            config_path = cls.DEFAULT_CONFIG_PATH
        
        config_path = os.path.expanduser(config_path)
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    parser = JsonComment()
                    config = parser.load(f)
                    # Merge with defaults to ensure all keys exist
                    return cls._merge_configs(cls.DEFAULT_CONFIG, config)
            except Exception as e:
                print(f"Warning: Failed to load config from {config_path}: {e}")
                print("Using default configuration...")
                return cls.DEFAULT_CONFIG.copy()
        else:
            return cls.DEFAULT_CONFIG.copy()
    
    @classmethod
    def create_default_config(cls, config_path=None):
        """Create default configuration file"""
        if config_path is None:
            config_path = cls.DEFAULT_CONFIG_PATH
        
        config_path = os.path.expanduser(config_path)
        config_dir = os.path.dirname(config_path)
        
        # Create directory if it doesn't exist
        Path(config_dir).mkdir(parents=True, exist_ok=True)
        
        # Write default config with comments
        with open(config_path, 'w') as f:
            f.write("// AnimatedFetching Configuration File\n")
            f.write("// This file uses JSONC format (JSON with Comments)\n\n")
            json.dump(cls.DEFAULT_CONFIG, f, indent=2)
        
        print(f"Created default configuration at: {config_path}")
        return config_path
    
    @staticmethod
    def _merge_configs(default, user):
        """Recursively merge user config with defaults"""
        result = default.copy()
        for key, value in user.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = Config._merge_configs(result[key], value)
            else:
                result[key] = value
        return result
