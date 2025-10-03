#!/usr/bin/env python3
"""
Animated GIF display module for AnimatedFetching
"""

import os
import time
from threading import Thread, Event
from PIL import Image
from rich.console import Console
from rich.align import Align

class AnimatedGIF:
    """Handles animated GIF display in terminal"""
    
    def __init__(self, gif_path, width=40, fps=10):
        self.gif_path = os.path.expanduser(gif_path)
        self.width = width
        self.fps = fps
        self.frames = []
        self.frame_durations = []  # Store duration for each frame
        self.stop_event = Event()
        self.thread = None
        self.current_frame = 0
        
        if os.path.exists(self.gif_path):
            self._load_frames()
    
    def _load_frames(self):
        """Load and convert GIF frames to ASCII/block characters"""
        try:
            img = Image.open(self.gif_path)
            frame_count = 0
            
            while True:
                try:
                    # Get frame duration (in milliseconds, default to 100ms if not specified)
                    duration = img.info.get('duration', 100) / 1000.0  # Convert to seconds
                    self.frame_durations.append(duration)
                    
                    # Resize frame
                    aspect_ratio = img.height / img.width
                    new_height = int(self.width * aspect_ratio * 0.5)  # 0.5 for char aspect ratio
                    frame = img.resize((self.width, new_height))
                    
                    # Convert to ASCII art representation
                    ascii_frame = self._image_to_ascii(frame)
                    self.frames.append(ascii_frame)
                    
                    frame_count += 1
                    img.seek(frame_count)
                except EOFError:
                    break
        except Exception as e:
            print(f"Error loading GIF: {e}")
    
    def _image_to_ascii(self, image):
        """Convert image to colored block characters"""
        # Convert to RGB
        image = image.convert('RGB')
        pixels = image.load()
        
        lines = []
        for y in range(image.height):
            line = ""
            for x in range(image.width):
                r, g, b = pixels[x, y]
                # Use block character with color
                line += f"\033[38;2;{r};{g};{b}m█\033[0m"
            lines.append(line)
        
        return "\n".join(lines)
    
    def get_static_frame(self):
        """Get first frame for static display"""
        if self.frames:
            return self.frames[0]
        return ""
    
    def get_current_frame(self):
        """Get current frame for animation"""
        if self.frames:
            return self.frames[self.current_frame]
        return ""
    
    def get_frame_count(self):
        """Get total number of frames"""
        return len(self.frames)
    
    def next_frame(self):
        """Advance to next frame and return its duration"""
        if not self.frames:
            return 0.1
        
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        
        # Use frame-specific duration or fallback to fps-based timing
        if self.frame_durations and self.current_frame < len(self.frame_durations):
            return self.frame_durations[self.current_frame]
        else:
            return 1.0 / self.fps
    
    def reset(self):
        """Reset animation to first frame"""
        self.current_frame = 0
