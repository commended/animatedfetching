# AnimatedFetching Examples

This document provides real-world examples and use cases for AnimatedFetching.

## Example 1: Minimal Setup

For users who want a simple, fast fetch program:

```jsonc
{
  "animation": {
    "enabled": false
  },
  "info_sections": [
    {"label": "OS", "key": "os", "color": "cyan"},
    {"label": "Uptime", "key": "uptime", "color": "green"},
    {"label": "Memory", "key": "memory", "color": "yellow"}
  ],
  "buttons": [],
  "layout": {
    "title": "Quick Info",
    "show_hostname": true
  }
}
```

Run: `afetch`

## Example 2: Developer Workstation

Configuration for developers with quick access to common commands:

```jsonc
{
  "animation": {
    "enabled": true,
    "path": "~/.config/animatedfetching/dev-logo.gif",
    "width": 35
  },
  "info_sections": [
    {"label": "Host", "key": "hostname", "color": "bright_cyan"},
    {"label": "OS", "key": "os", "color": "cyan"},
    {"label": "Kernel", "key": "kernel", "color": "blue"},
    {"label": "Shell", "key": "shell", "color": "yellow"},
    {"label": "CPU", "key": "cpu", "color": "red"},
    {"label": "Memory", "key": "memory", "color": "green"}
  ],
  "buttons": [
    {
      "label": "Git Status",
      "command": "git status -sb && echo && git log --oneline -5",
      "key": "g",
      "color": "yellow"
    },
    {
      "label": "Docker Containers",
      "command": "docker ps -a",
      "key": "d",
      "color": "blue"
    },
    {
      "label": "Port Usage",
      "command": "sudo lsof -i -P -n | grep LISTEN",
      "key": "p",
      "color": "magenta"
    },
    {
      "label": "NPM Scripts",
      "command": "npm run",
      "key": "n",
      "color": "red"
    },
    {
      "label": "VS Code",
      "command": "code .",
      "key": "c",
      "color": "cyan"
    }
  ],
  "layout": {
    "title": "Developer Dashboard",
    "show_hostname": true,
    "separator": "━",
    "padding": 2
  }
}
```

Run: `afetch -i` and press keys to execute commands

## Example 3: System Administrator

Configuration for sysadmins with monitoring and management tools:

```jsonc
{
  "animation": {
    "enabled": false
  },
  "info_sections": [
    {"label": "Hostname", "key": "hostname", "color": "bright_green"},
    {"label": "OS", "key": "os", "color": "cyan"},
    {"label": "Kernel", "key": "kernel", "color": "blue"},
    {"label": "Uptime", "key": "uptime", "color": "green"},
    {"label": "CPU", "key": "cpu", "color": "red"},
    {"label": "Memory", "key": "memory", "color": "yellow"},
    {"label": "Disk", "key": "disk", "color": "magenta"}
  ],
  "buttons": [
    {
      "label": "System Status",
      "command": "systemctl status",
      "key": "s",
      "color": "cyan"
    },
    {
      "label": "Active Services",
      "command": "systemctl list-units --type=service --state=running",
      "key": "a",
      "color": "green"
    },
    {
      "label": "Failed Services",
      "command": "systemctl --failed",
      "key": "f",
      "color": "red"
    },
    {
      "label": "Network Connections",
      "command": "ss -tulpn",
      "key": "n",
      "color": "blue"
    },
    {
      "label": "Disk Usage Detail",
      "command": "df -h && echo && du -sh /* 2>/dev/null | sort -rh | head -10",
      "key": "d",
      "color": "yellow"
    },
    {
      "label": "Process Monitor",
      "command": "htop",
      "key": "p",
      "color": "magenta"
    },
    {
      "label": "System Logs",
      "command": "journalctl -xe --no-pager -n 50",
      "key": "l",
      "color": "white"
    },
    {
      "label": "Update System",
      "command": "sudo apt update && sudo apt upgrade -y",
      "key": "u",
      "color": "bright_green"
    }
  ],
  "layout": {
    "title": "System Administration Panel",
    "show_hostname": true,
    "separator": "═",
    "padding": 2
  },
  "colors": {
    "title": "bold bright_cyan",
    "label": "bold",
    "separator": "dim"
  }
}
```

## Example 4: Server Monitoring

Lightweight config for SSH sessions to remote servers:

```jsonc
{
  "animation": {
    "enabled": false
  },
  "info_sections": [
    {"label": "Host", "key": "hostname", "color": "bright_yellow"},
    {"label": "OS", "key": "os", "color": "cyan"},
    {"label": "Uptime", "key": "uptime", "color": "green"},
    {"label": "CPU", "key": "cpu", "color": "red"},
    {"label": "Memory", "key": "memory", "color": "yellow"},
    {"label": "Disk", "key": "disk", "color": "magenta"}
  ],
  "buttons": [
    {
      "label": "Quick Status",
      "command": "uptime && echo && free -h && echo && df -h /",
      "key": "q",
      "color": "cyan"
    },
    {
      "label": "Network Test",
      "command": "ping -c 4 8.8.8.8",
      "key": "n",
      "color": "blue"
    },
    {
      "label": "Who's Logged In",
      "command": "who && echo && last -10",
      "key": "w",
      "color": "yellow"
    }
  ],
  "layout": {
    "title": "Server Status",
    "show_hostname": true
  }
}
```

Add to `.bashrc` or `.zshrc`: `alias status='afetch'`

## Example 5: Gaming Setup

Fun configuration with ASCII art and gaming utilities:

```jsonc
{
  "animation": {
    "enabled": true,
    "path": "~/.config/animatedfetching/gaming.gif",
    "width": 50,
    "fps": 15
  },
  "info_sections": [
    {"label": "System", "key": "os", "color": "bright_magenta"},
    {"label": "CPU", "key": "cpu", "color": "bright_red"},
    {"label": "Memory", "key": "memory", "color": "bright_yellow"},
    {"label": "Uptime", "key": "uptime", "color": "bright_green"}
  ],
  "buttons": [
    {
      "label": "Steam",
      "command": "steam",
      "key": "s",
      "color": "blue"
    },
    {
      "label": "Discord",
      "command": "discord",
      "key": "d",
      "color": "bright_blue"
    },
    {
      "label": "GPU Info",
      "command": "nvidia-smi",
      "key": "g",
      "color": "green"
    },
    {
      "label": "Game Servers",
      "command": "ping -c 3 game-server.example.com",
      "key": "p",
      "color": "yellow"
    }
  ],
  "layout": {
    "title": "⚡ GAMING STATION ⚡",
    "show_hostname": true,
    "separator": "▬",
    "padding": 2
  },
  "colors": {
    "title": "bold bright_magenta",
    "label": "bold bright_cyan",
    "separator": "bright_blue"
  }
}
```

## Example 6: Raspberry Pi / IoT Device

Compact view for resource-constrained devices:

```jsonc
{
  "animation": {
    "enabled": false
  },
  "info_sections": [
    {"label": "Device", "key": "hostname", "color": "green"},
    {"label": "OS", "key": "os", "color": "cyan"},
    {"label": "Uptime", "key": "uptime", "color": "yellow"},
    {"label": "CPU Temp", "key": "cpu", "color": "red"},
    {"label": "Memory", "key": "memory", "color": "magenta"},
    {"label": "Disk", "key": "disk", "color": "blue"}
  ],
  "buttons": [
    {
      "label": "Temperature",
      "command": "vcgencmd measure_temp",
      "key": "t",
      "color": "red"
    },
    {
      "label": "GPIO Status",
      "command": "gpio readall",
      "key": "g",
      "color": "green"
    },
    {
      "label": "Network",
      "command": "ifconfig",
      "key": "n",
      "color": "cyan"
    },
    {
      "label": "Reboot",
      "command": "sudo reboot",
      "key": "r",
      "color": "red"
    }
  ],
  "layout": {
    "title": "🔧 Pi Status",
    "show_hostname": true
  }
}
```

## Tips for Creating Custom Configurations

1. **Test commands first**: Always test your commands in the terminal before adding them to buttons
2. **Use command chains**: Combine multiple commands with `&&` for comprehensive outputs
3. **Add aliases**: Create shell aliases for frequently used configs
4. **Customize colors**: Match your terminal theme for a cohesive look
5. **Keep it focused**: Don't add too many buttons - keep the most useful ones
6. **Use clear labels**: Make button labels descriptive but concise

## Adding to Shell Startup

Add to your `.bashrc`, `.zshrc`, or `.profile`:

```bash
# Show system info on terminal startup
if command -v afetch &> /dev/null; then
    afetch
fi
```

Or for interactive mode:
```bash
alias sysinfo='afetch -i'
```

## Integration with Other Tools

### With tmux
Add to `.tmux.conf`:
```
bind-key i run-shell "tmux display-popup -E 'afetch -i'"
```

### With i3/sway
Add to config:
```
bindsym $mod+i exec --no-startup-id alacritty -e afetch -i
```

### As a Motd (Message of the Day)
Create `/etc/profile.d/animatedfetching.sh`:
```bash
#!/bin/bash
if [ -n "$SSH_CONNECTION" ]; then
    /usr/local/bin/afetch
fi
```
