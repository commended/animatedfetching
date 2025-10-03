#!/usr/bin/env python3
"""
Main application module for AnimatedFetching
"""

import sys
import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
from rich.layout import Layout
from rich.table import Table
from rich.prompt import Prompt

from .config import Config
from .sysinfo import SystemInfo
from .animation import AnimatedGIF


class AnimatedFetching:
    """Main application class"""
    
    def __init__(self, config_path=None):
        self.console = Console()
        self.config = Config.load(config_path)
        self.sysinfo = SystemInfo.get_all()
        
        # Load animation if enabled
        self.animation = None
        if self.config.get('animation', {}).get('enabled', False):
            gif_path = self.config['animation'].get('path')
            if gif_path and os.path.exists(os.path.expanduser(gif_path)):
                self.animation = AnimatedGIF(
                    gif_path,
                    width=self.config['animation'].get('width', 40),
                    fps=self.config['animation'].get('fps', 10)
                )
    
    def render_info_section(self):
        """Render system information section"""
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Label", style="bold")
        table.add_column("Value")
        
        # Add hostname if configured
        if self.config.get('layout', {}).get('show_hostname', True):
            hostname = self.sysinfo.get('hostname', 'unknown')
            table.add_row(
                Text("Host", style=self.config.get('colors', {}).get('title', 'bold cyan')),
                Text(hostname, style="bold")
            )
            
            # Add separator
            separator = self.config.get('layout', {}).get('separator', '─')
            table.add_row(Text(separator * 40, style="dim"), "")
        
        # Add configured info sections
        for section in self.config.get('info_sections', []):
            key = section.get('key')
            label = section.get('label', key)
            color = section.get('color', 'white')
            
            if key in self.sysinfo:
                value = self.sysinfo[key]
                table.add_row(
                    Text(label, style=f"bold {color}"),
                    Text(str(value))
                )
        
        return table
    
    def render_buttons(self):
        """Render clickable buttons section"""
        if not self.config.get('buttons'):
            return None
        
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Key", style="bold")
        table.add_column("Action")
        
        for button in self.config['buttons']:
            key = button.get('key', '')
            label = button.get('label', 'Unknown')
            color = button.get('color', 'white')
            
            table.add_row(
                Text(f"[{key}]", style=f"bold {color}"),
                Text(label)
            )
        
        return Panel(
            table,
            title="[bold]Actions[/bold]",
            border_style="blue"
        )
    
    def display(self):
        """Display the fetch information"""
        # Clear screen
        self.console.clear()
        
        # Create title
        title = self.config.get('layout', {}).get('title', 'System Information')
        title_style = self.config.get('colors', {}).get('title', 'bold cyan')
        
        self.console.print(f"\n[{title_style}]{title}[/{title_style}]\n")
        
        # Display animation and info side by side if animation exists
        if self.animation:
            frame = self.animation.get_static_frame()
            if frame:
                # Split screen layout
                info_table = self.render_info_section()
                
                # Print side by side (simplified version)
                self.console.print(info_table)
            else:
                self.console.print(self.render_info_section())
        else:
            self.console.print(self.render_info_section())
        
        # Display buttons
        buttons_panel = self.render_buttons()
        if buttons_panel:
            self.console.print("\n")
            self.console.print(buttons_panel)
        
        self.console.print("")
    
    def run_interactive(self):
        """Run in interactive mode with button support"""
        self.display()
        
        if not self.config.get('buttons'):
            return
        
        self.console.print("[dim]Press a key to run an action, or 'q' to quit[/dim]")
        
        # Create key mapping
        key_map = {}
        for button in self.config['buttons']:
            key = button.get('key')
            if key:
                key_map[key] = button
        
        while True:
            try:
                choice = Prompt.ask("\nChoice", default="q")
                
                if choice.lower() == 'q':
                    break
                
                if choice in key_map:
                    button = key_map[choice]
                    command = button.get('command')
                    if command:
                        self.console.print(f"\n[bold green]Running:[/bold green] {command}\n")
                        try:
                            # Run command in interactive shell
                            subprocess.run(command, shell=True)
                        except Exception as e:
                            self.console.print(f"[bold red]Error:[/bold red] {e}")
                        
                        self.console.print("\n[dim]Press Enter to continue...[/dim]")
                        input()
                        self.display()
                        self.console.print("[dim]Press a key to run an action, or 'q' to quit[/dim]")
                else:
                    self.console.print("[yellow]Invalid choice. Try again.[/yellow]")
            
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted[/yellow]")
                break
            except EOFError:
                break
    
    def run(self):
        """Run the application (non-interactive)"""
        self.display()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='AnimatedFetching - A terminal fetch program with animated GIF support'
    )
    parser.add_argument(
        '-c', '--config',
        help='Path to configuration file',
        default=None
    )
    parser.add_argument(
        '--create-config',
        action='store_true',
        help='Create default configuration file'
    )
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Run in interactive mode with button support'
    )
    
    args = parser.parse_args()
    
    if args.create_config:
        config_path = Config.create_default_config(args.config)
        sys.exit(0)
    
    try:
        app = AnimatedFetching(config_path=args.config)
        
        if args.interactive:
            app.run_interactive()
        else:
            app.run()
    
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
