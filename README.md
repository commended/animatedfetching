# AnimatedFetching

A fast terminal fetch program written in C with GIF logo support. Inspired by fastfetch.

## Features

- 🎨 **GIF Logo Support**: Display GIF images as logos in your terminal
- 🚀 **Fast & Lightweight**: Written in C, minimal dependencies
- 📊 **System Information**: OS, kernel, uptime, CPU, memory, and more
- 🎯 **Centered Layout**: Clean, centered display
- 🖥️ **True Color**: Full 24-bit RGB color support

## Installation

### One-Line Install

```bash
git clone https://github.com/commended/animatedfetching.git && cd animatedfetching && ./setup.sh && sudo make install
```

### Step-by-Step Install

```bash
# 1. Clone and setup
git clone https://github.com/commended/animatedfetching.git
cd animatedfetching

# 2. Install dependencies
# Debian/Ubuntu:
sudo apt install libgif-dev

# Fedora:
sudo dnf install giflib-devel

# Arch:
sudo pacman -S giflib

# 3. Build and install globally
./setup.sh
sudo make install
```

The setup script will:
- Build the program
- Create `~/.config/animatedfetching/` directory
- Install the default GIF animation

After installation, you can run `afetch` from anywhere.

## Usage

Run `afetch` to display your system information:

```bash
afetch
```

### Custom GIF

Use a custom GIF file:

```bash
afetch --gif /path/to/your/animation.gif
# or
afetch -g /path/to/your/animation.gif
```

Set your default GIF:

```bash
cp your-logo.gif ~/.config/animatedfetching/animation.gif
```

## Updating

To update to the latest version:

```bash
cd animatedfetching
git pull
make clean
make
sudo make install
```

## Uninstalling

To remove AnimatedFetching:

```bash
sudo make uninstall
```

Optionally remove the configuration directory:

```bash
rm -rf ~/.config/animatedfetching
```

## Command Line Options

```
Usage: afetch [OPTIONS]

Options:
  -g, --gif <path>    Path to GIF file (default: ~/.config/animatedfetching/animation.gif)
  -h, --help          Show this help message
```

## Tips

1. **Add your own GIF**: Place any GIF at `~/.config/animatedfetching/animation.gif`
2. **Terminal compatibility**: Works best with terminals that support 24-bit RGB colors
3. **GIF size**: Keep GIFs under 1MB for faster loading
4. **Animation**: Currently displays the first frame of animated GIFs (static display)

## Technical Details

- **Language**: C11
- **Dependencies**: giflib only
- **System Info**: Direct system calls and `/proc` filesystem parsing
- **Rendering**: 24-bit RGB ANSI escape codes

For more details, see [DESIGN.md](DESIGN.md).

## License

MIT License

## Author

Designed by aug
