#!/bin/bash
# Setup script for AnimatedFetching

set -e

echo "AnimatedFetching Setup"
echo "====================="
echo ""

# Check for giflib
echo "Checking dependencies..."
if ! ldconfig -p | grep -q libgif; then
    echo "Error: libgif not found!"
    echo ""
    echo "Please install giflib:"
    echo "  Ubuntu/Debian: sudo apt install libgif-dev"
    echo "  Fedora:        sudo dnf install giflib-devel"
    echo "  Arch:          sudo pacman -S giflib"
    echo ""
    exit 1
fi

echo "✓ Dependencies found"
echo ""

# Build
echo "Building afetch..."
make clean
make
echo ""

# Create config directory
echo "Setting up configuration directory..."
CONFIG_DIR="$HOME/.config/animatedfetching"
mkdir -p "$CONFIG_DIR"
echo "✓ Created $CONFIG_DIR"

# Copy default GIF if it doesn't exist
if [ -f "animatedfetching/resources/default_animation.gif" ]; then
    if [ ! -f "$CONFIG_DIR/animation.gif" ]; then
        cp animatedfetching/resources/default_animation.gif "$CONFIG_DIR/animation.gif"
        echo "✓ Installed default animation GIF"
    else
        echo "✓ Animation GIF already exists"
    fi
fi

echo ""
echo "Setup complete!"
echo ""
echo "You can now run: ./bin/afetch"
echo "Or install system-wide with: sudo make install"
echo ""
