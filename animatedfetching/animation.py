#!/usr/bin/env python3
"""
Animated GIF display module for AnimatedFetching
"""

import os
import time
from threading import Thread, Event
from PIL import Image
from rich.console import Console

class AnimatedGIF:
    """Handles animated GIF display in terminal"""
    
    def __init__(self, gif_path, width=40, fps=10):
        self.gif_path = os.path.expanduser(gif_path)
        self.width = width
        self.fps = fps
        self.frames = []
        self.stop_event = Event()
        self.thread = None
        
        if os.path.exists(self.gif_path):
            self._load_frames()
    
    def _load_frames(self):
        """Load and convert GIF frames to ASCII/block characters"""
        try:
            img = Image.open(self.gif_path)
            frame_count = 0
            
            while True:
                try:
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
    
    def start_animation(self, console):
        """Start animated display in a separate thread"""
        if not self.frames:
            return
        
        def animate():
            frame_idx = 0
            while not self.stop_event.is_set():
                # This would need to be integrated with the main display
                # For now, we'll return frames for static display
                time.sleep(1.0 / self.fps)
                frame_idx = (frame_idx + 1) % len(self.frames)
        
        self.thread = Thread(target=animate, daemon=True)
        self.thread.start()
    
    def stop_animation(self):
        """Stop the animation"""
        self.stop_event.set()
        if self.thread:
            self.thread.join(timeout=1.0)
