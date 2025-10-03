# AnimatedFetching

An animated terminal fetch program written in C, designed by aug with animated GIF support. Inspired by fastfetch, with GIF logo display centered above system information.

## Quick Start

Get started in 3 simple steps:

```bash
# 1. Clone and build
git clone https://github.com/commended/animatedfetching.git
cd animatedfetching
make

# 2. Run it!
./bin/afetch
```

That's it! The program will display your system information with the GIF logo centered above it.

## Features

- 🎨 **Animated GIF Support**: Display animated GIFs as logos in your terminal
- 🚀 **Written in C**: Fast and lightweight, inspired by fastfetch
- 📊 **System Information**: Display OS, kernel, uptime, CPU, memory, and more
- 🎯 **Centered Layout**: GIF displayed on top, system info centered below
- 🖥️ **Terminal Colors**: Full 24-bit RGB color support for GIF rendering

## Installation

### Build from Source

```bash
git clone https://github.com/commended/animatedfetching.git
cd animatedfetching
make
```

### Install System-wide

```bash
sudo make install
```

This installs the binary to `/usr/local/bin/afetch`.

### Dependencies

The following libraries are required:
- giflib (libgif-dev on Debian/Ubuntu, giflib-devel on Fedora)

Install on Debian/Ubuntu:
```bash
sudo apt install libgif-dev
```

Install on Fedora:
```bash
sudo dnf install giflib-devel
```

Install on Arch:
```bash
sudo pacman -S giflib
```

## Usage

### Basic Usage

Display system information with GIF logo:

```bash
./bin/afetch
# or if installed system-wide:
afetch
```

### Custom GIF

Use a custom GIF file:

```bash
afetch --gif /path/to/your/animation.gif
# or
afetch -g /path/to/your/animation.gif
```

The default GIF location is `~/.config/animatedfetching/animation.gif`.

## How It Works

AnimatedFetching is a C program that:

1. **Gathers System Information**: Uses Linux system calls to collect information about your system (hostname, OS, kernel, uptime, shell, terminal, CPU, memory)
2. **Loads GIF Files**: Uses the giflib library to load and decode GIF images
3. **Renders in Terminal**: Converts GIF pixels to colored block characters (█) using 24-bit RGB ANSI escape codes
4. **Centers Output**: Calculates terminal width and centers both the GIF and system information

The implementation is inspired by fastfetch's approach to system information gathering, with added GIF rendering capabilities.

## Command Line Options

```
Usage: afetch [OPTIONS]

AnimatedFetching - A terminal fetch program with GIF support

Options:
  -g, --gif <path>    Path to GIF file (default: ~/.config/animatedfetching/animation.gif)
  -h, --help          Show this help message
```

## Examples

### Display with default GIF:
```bash
afetch
```

### Use custom GIF:
```bash
afetch --gif ~/Pictures/my-logo.gif
```

### Setup default GIF location:
```bash
mkdir -p ~/.config/animatedfetching
cp my-animation.gif ~/.config/animatedfetching/animation.gif
afetch
```

## Tips

1. **Add your own GIF**: Place any GIF file at `~/.config/animatedfetching/animation.gif`
2. **Terminal compatibility**: Best viewed in terminals with 24-bit RGB color support (most modern terminals)
3. **GIF size**: Keep GIFs reasonably sized (under 1MB) for faster loading
4. **First frame**: Currently displays only the first frame of animated GIFs (static display)

## License

MIT License

## Author

Designed by aug
