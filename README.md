# AnimatedFetching

An animated terminal fetch program designed by aug with animated GIF support, customizable configuration, and clickable buttons for running commands.

## Features

- 🎨 **Animated GIF Support**: Display animated GIFs in your terminal alongside system information
- 🔧 **Highly Customizable**: Configure everything via JSONC files (JSON with Comments)
- 🖱️ **Interactive Buttons**: Clickable buttons to run terminal commands
- 📊 **System Information**: Display OS, kernel, uptime, CPU, memory, disk, and more
- 🎯 **Fastfetch-like**: Similar configuration style and functionality to fastfetch

## Installation

### From Source

```bash
git clone https://github.com/commended/animatedfetching.git
cd animatedfetching
pip install -e .
```

### Dependencies

The following Python packages are required:
- rich >= 13.0.0
- Pillow >= 10.0.0
- psutil >= 5.9.0
- distro >= 1.8.0
- jsoncomment >= 0.4.2

## Usage

### Basic Usage

Display system information:

```bash
animatedfetching
# or use the short alias
afetch
```

### Interactive Mode

Run in interactive mode with clickable buttons:

```bash
animatedfetching --interactive
# or
afetch -i
```

In interactive mode, you can press the configured keys (e.g., 'u', 'n', 'd', 't') to run the associated commands.

### Create Default Configuration

Create a default configuration file at `~/.config/animatedfetching/config.jsonc`:

```bash
animatedfetching --create-config
```

### Use Custom Configuration

```bash
animatedfetching --config /path/to/config.jsonc
```

## Configuration

Configuration is stored in JSONC format (JSON with Comments) at:
`~/.config/animatedfetching/config.jsonc`

### Example Configuration

```jsonc
{
  // Animation settings
  "animation": {
    "enabled": true,
    "path": "~/.config/animatedfetching/animation.gif",
    "width": 40,
    "fps": 10
  },
  
  // System information sections to display
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
  
  // Interactive buttons
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
  
  // Layout settings
  "layout": {
    "title": "System Information",
    "show_hostname": true,
    "separator": "─",
    "padding": 2
  },
  
  // Color scheme
  "colors": {
    "title": "bold cyan",
    "label": "bold",
    "separator": "dim"
  }
}
```

### Configuration Options

#### Animation Section
- `enabled`: Enable/disable animated GIF display
- `path`: Path to your GIF file (supports `~` expansion)
- `width`: Width of the animation in characters (default: 40)
- `fps`: Frames per second for animation (default: 10)

#### Info Sections
Each section has:
- `label`: Display name for the information
- `key`: System info key (os, kernel, uptime, shell, terminal, cpu, memory, disk, hostname)
- `color`: Color for the label (cyan, blue, green, yellow, magenta, red, white, etc.)

#### Buttons
Each button has:
- `label`: Display name for the button
- `command`: Shell command to run when button is pressed
- `key`: Keyboard shortcut (single character)
- `color`: Color for the button display

#### Layout Options
- `title`: Title displayed at the top
- `show_hostname`: Show hostname in the info display
- `separator`: Character(s) to use as separator
- `padding`: Padding around elements

#### Colors
- `title`: Style for the title
- `label`: Style for labels
- `separator`: Style for separators

## Command Line Options

```
usage: animatedfetching [-h] [-c CONFIG] [--create-config] [-i]

AnimatedFetching - A terminal fetch program with animated GIF support

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Path to configuration file
  --create-config       Create default configuration file
  -i, --interactive     Run in interactive mode with button support
```

## Examples

### Display system info with default config:
```bash
animatedfetching
```

### Run interactively:
```bash
animatedfetching -i
```

### Use custom config:
```bash
animatedfetching -c ~/my-custom-config.jsonc
```

### Create default config:
```bash
animatedfetching --create-config
```

## Tips

1. **Add your own GIF**: Place any GIF file at `~/.config/animatedfetching/animation.gif` or configure a custom path
2. **Customize buttons**: Add your own frequently-used commands as buttons
3. **Color schemes**: Use any Rich library color names (cyan, blue, green, yellow, magenta, red, bright_blue, etc.)
4. **Info sections**: Reorder sections in the config to change display order

## License

MIT License

## Author

Designed by aug
