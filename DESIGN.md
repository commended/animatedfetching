# AnimatedFetching - Design Documentation

## Overview

AnimatedFetching is a C implementation of a terminal fetch program with GIF logo support. It was designed to be fast, lightweight, and inspired by fastfetch's approach to system information gathering.

## Architecture

### Core Components

1. **System Information Gathering** (`sysinfo.c`)
   - Uses Linux system calls and `/proc` filesystem
   - Inspired by fastfetch's efficient approach
   - Collects: hostname, OS, kernel, uptime, shell, terminal, CPU, memory

2. **GIF Rendering** (`render.c`)
   - Uses `giflib` to decode GIF images
   - Converts pixels to colored block characters (█)
   - Uses 24-bit RGB ANSI escape codes for true color
   - Scales GIF to fit terminal width (max 40 characters)

3. **Main Application** (`main.c`)
   - Handles command-line arguments
   - Coordinates GIF loading and info display
   - Manages layout and centering

### Design Decisions

#### Why C?
- **Performance**: C provides direct system access with minimal overhead
- **Simplicity**: No runtime dependencies beyond standard libraries and giflib
- **Fastfetch Inspiration**: Following fastfetch's lead, which is also written in C
- **Portability**: C code is highly portable across Unix-like systems

#### GIF Rendering Approach
- **Static Frame Only**: Currently displays only the first frame of GIFs
  - Simplifies implementation
  - Avoids complex threading and terminal control
  - Still provides the visual logo branding
  - Future versions could add animation support

- **Block Characters**: Using `█` (full block) with RGB colors
  - Simple and effective
  - Works in most modern terminals
  - Better than ASCII art for color fidelity

#### Layout Strategy
- **Top Padding**: Adds vertical space at top for visual balance
- **Centered Content**: Both GIF and info are centered horizontally
- **GIF Above Info**: Logo/branding first, then system details
- **Consistent Spacing**: Uniform padding throughout

### System Information Sources

Following fastfetch's approach, information is gathered from:

- **Hostname**: `gethostname()` system call
- **OS**: `/etc/os-release` file (PRETTY_NAME field)
- **Kernel**: `uname()` system call (release field)
- **Uptime**: `sysinfo()` system call
- **Shell**: `$SHELL` environment variable
- **Terminal**: `$TERM` environment variable
- **CPU**: `/proc/cpuinfo` file (model name field)
- **Memory**: `sysinfo()` system call (RAM usage)

### Color Scheme

Using ANSI escape codes:
- **Cyan (36)**: Hostname, OS
- **Blue (34)**: Kernel
- **Green (32)**: Uptime
- **Yellow (33)**: Shell
- **Magenta (35)**: Terminal
- **Red (31)**: CPU
- **Bold (1)**: All labels

### Error Handling

- **Missing GIF**: Displays warning but continues with info display
- **Failed GIF Load**: Shows error message but program continues
- **Missing System Info**: Falls back to "Unknown" values
- **Terminal Width**: Defaults to 80 columns if detection fails

## Future Enhancements

Potential improvements for future versions:

1. **Animation Support**
   - Multi-frame GIF animation in terminal
   - Frame timing from GIF metadata
   - Requires terminal manipulation (ANSI cursor control)

2. **Configuration File**
   - Color customization
   - Info field selection/ordering
   - GIF display options (size, position)

3. **Additional Info Fields**
   - Disk usage
   - GPU information
   - Package counts
   - Desktop environment/window manager

4. **Logo Library**
   - Built-in logos for popular distros
   - Automatic logo selection based on OS

5. **Performance Optimizations**
   - Caching GIF frames
   - Parallel system info gathering
   - Memory pooling

## Building and Testing

### Build Requirements
- GCC or compatible C compiler
- GNU Make
- giflib development headers

### Testing Checklist
- [ ] Compile without warnings
- [ ] Run with valid GIF file
- [ ] Run without GIF file (fallback)
- [ ] Test on different terminal emulators
- [ ] Test with various GIF sizes
- [ ] Verify centering on different terminal widths
- [ ] Check memory leaks with valgrind

## Contributing

When contributing to AnimatedFetching:

1. Maintain the minimal, efficient design philosophy
2. Follow fastfetch's example for system info gathering
3. Keep external dependencies minimal
4. Test on multiple platforms/terminals
5. Document any new features or changes

## License

MIT License - See LICENSE file for details
