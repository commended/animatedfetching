# Installation and Usage Guide

## Quick Start

### 1. Install the package

```bash
# Clone the repository
git clone https://github.com/commended/animatedfetching.git
cd animatedfetching

# Install dependencies and the package
pip install -e .
```

### 2. Create default configuration

```bash
animatedfetching --create-config
```

This creates `~/.config/animatedfetching/config.jsonc` with default settings.

### 3. Run the program

```bash
# Basic mode - display system info
animatedfetching

# Or use the short alias
afetch

# Interactive mode - with clickable buttons
animatedfetching -i
```

## Adding Custom GIF

1. Find or create an animated GIF
2. Place it at `~/.config/animatedfetching/animation.gif`
3. Or configure a custom path in the config file:

```jsonc
{
  "animation": {
    "enabled": true,
    "path": "/path/to/your/animation.gif",
    "width": 40,
    "fps": 10
  }
}
```

## Customizing Buttons

Edit `~/.config/animatedfetching/config.jsonc` and modify the `buttons` array:

```jsonc
{
  "buttons": [
    {
      "label": "My Custom Command",
      "command": "echo 'Hello World'",
      "key": "h",
      "color": "green"
    }
  ]
}
```

Then run in interactive mode:
```bash
animatedfetching -i
```

Press 'h' to run your custom command!

## Customizing Info Sections

You can reorder, add, or remove info sections:

```jsonc
{
  "info_sections": [
    {"label": "Operating System", "key": "os", "color": "cyan"},
    {"label": "Kernel Version", "key": "kernel", "color": "blue"},
    {"label": "System Uptime", "key": "uptime", "color": "green"}
  ]
}
```

Available keys:
- `hostname` - System hostname
- `os` - Operating system name and version
- `kernel` - Kernel version
- `uptime` - System uptime
- `shell` - Current shell
- `terminal` - Terminal emulator
- `cpu` - CPU model
- `memory` - Memory usage
- `disk` - Disk usage

## Color Options

Available colors for `color` fields:
- Basic: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- Bright: `bright_black`, `bright_red`, `bright_green`, etc.
- Styles: `bold`, `dim`, `italic`, `underline`
- Combined: `bold cyan`, `dim red`, etc.

## Examples

### Minimal Configuration

```jsonc
{
  "animation": {
    "enabled": false
  },
  "info_sections": [
    {"label": "OS", "key": "os", "color": "cyan"},
    {"label": "Uptime", "key": "uptime", "color": "green"}
  ],
  "buttons": [],
  "layout": {
    "title": "System Info"
  }
}
```

### Developer Configuration

```jsonc
{
  "buttons": [
    {
      "label": "Git Status",
      "command": "git status",
      "key": "g",
      "color": "yellow"
    },
    {
      "label": "Docker PS",
      "command": "docker ps",
      "key": "d",
      "color": "blue"
    },
    {
      "label": "NPM Test",
      "command": "npm test",
      "key": "t",
      "color": "green"
    }
  ]
}
```

### System Admin Configuration

```jsonc
{
  "buttons": [
    {
      "label": "Service Status",
      "command": "systemctl status",
      "key": "s",
      "color": "cyan"
    },
    {
      "label": "Network Connections",
      "command": "ss -tulpn",
      "key": "n",
      "color": "blue"
    },
    {
      "label": "System Logs",
      "command": "journalctl -xe",
      "key": "l",
      "color": "yellow"
    }
  ]
}
```

## Troubleshooting

### Config file not found
Run `animatedfetching --create-config` to create the default configuration.

### GIF not displaying
1. Ensure the GIF file exists at the configured path
2. Check that `animation.enabled` is `true` in the config
3. Verify the GIF file is a valid animated GIF

### Commands not running in interactive mode
1. Make sure you run with `-i` flag: `animatedfetching -i`
2. Press the key assigned to the button (case-sensitive)
3. Check that the command is valid and executable

### Dependencies not installed
Run `pip install -r requirements.txt` to install all dependencies.
