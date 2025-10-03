#!/usr/bin/env python3
"""
AnimatedFetching - A terminal fetch program with animated GIF support
"""

import os
import sys
import platform
import psutil
import distro
import socket
from datetime import datetime

class SystemInfo:
    """Collects system information similar to fastfetch"""
    
    @staticmethod
    def get_os():
        """Get operating system name"""
        if platform.system() == "Linux":
            return f"{distro.name()} {distro.version()}"
        return f"{platform.system()} {platform.release()}"
    
    @staticmethod
    def get_kernel():
        """Get kernel version"""
        return platform.release()
    
    @staticmethod
    def get_hostname():
        """Get hostname"""
        return socket.gethostname()
    
    @staticmethod
    def get_uptime():
        """Get system uptime"""
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        
        return " ".join(parts) if parts else "0m"
    
    @staticmethod
    def get_shell():
        """Get current shell"""
        return os.environ.get('SHELL', 'unknown').split('/')[-1]
    
    @staticmethod
    def get_terminal():
        """Get terminal emulator"""
        return os.environ.get('TERM', 'unknown')
    
    @staticmethod
    def get_cpu():
        """Get CPU information"""
        try:
            with open('/proc/cpuinfo', 'r') as f:
                for line in f:
                    if 'model name' in line:
                        return line.split(':')[1].strip()
        except:
            pass
        return platform.processor() or "Unknown CPU"
    
    @staticmethod
    def get_memory():
        """Get memory usage"""
        mem = psutil.virtual_memory()
        used = mem.used / (1024 ** 3)  # Convert to GB
        total = mem.total / (1024 ** 3)
        return f"{used:.1f}GB / {total:.1f}GB ({mem.percent}%)"
    
    @staticmethod
    def get_disk():
        """Get disk usage"""
        try:
            disk = psutil.disk_usage('/')
            used = disk.used / (1024 ** 3)  # Convert to GB
            total = disk.total / (1024 ** 3)
            return f"{used:.1f}GB / {total:.1f}GB ({disk.percent}%)"
        except:
            return "Unknown"
    
    @staticmethod
    def get_all():
        """Get all system information"""
        return {
            'hostname': SystemInfo.get_hostname(),
            'os': SystemInfo.get_os(),
            'kernel': SystemInfo.get_kernel(),
            'uptime': SystemInfo.get_uptime(),
            'shell': SystemInfo.get_shell(),
            'terminal': SystemInfo.get_terminal(),
            'cpu': SystemInfo.get_cpu(),
            'memory': SystemInfo.get_memory(),
            'disk': SystemInfo.get_disk(),
        }
