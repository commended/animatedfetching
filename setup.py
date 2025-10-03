#!/usr/bin/env python3
"""
Setup script for AnimatedFetching
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="animatedfetching",
    version="1.0.0",
    author="aug",
    description="A terminal fetch program with animated GIF support and clickable buttons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/commended/animatedfetching",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0",
        "Pillow>=10.0.0",
        "psutil>=5.9.0",
        "distro>=1.8.0",
        "jsoncomment>=0.4.2",
    ],
    entry_points={
        "console_scripts": [
            "animatedfetching=animatedfetching.main:main",
            "afetch=animatedfetching.main:main",
        ],
    },
)
