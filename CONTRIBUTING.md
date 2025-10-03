# Contributing to AnimatedFetching

Thank you for your interest in contributing to AnimatedFetching! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/animatedfetching.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Install in development mode: `pip install -e .`

## Development Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tests
```bash
python test_animatedfetching.py
```

## Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

## Making Changes

### Adding New Features

1. Create a new branch for your feature
2. Implement your changes
3. Test your changes thoroughly
4. Update documentation if needed
5. Submit a pull request

### Adding New System Information

To add a new system information field:

1. Add a static method to `animatedfetching/sysinfo.py`:
```python
@staticmethod
def get_your_info():
    """Get your information"""
    # Implementation
    return "value"
```

2. Add to `get_all()` method:
```python
'your_info': SystemInfo.get_your_info(),
```

3. Update default config in `animatedfetching/config.py`

### Adding New Configuration Options

1. Add to `DEFAULT_CONFIG` in `animatedfetching/config.py`
2. Update `example-config.jsonc`
3. Document in README.md and USAGE.md
4. Test with custom configs

## Testing

Before submitting a pull request:

1. Run the test suite: `python test_animatedfetching.py`
2. Test basic functionality: `animatedfetching`
3. Test interactive mode: `animatedfetching -i`
4. Test config creation: `animatedfetching --create-config`
5. Test with custom config: `animatedfetching -c custom.jsonc`

## Documentation

When adding new features, update:

- `README.md` - Main documentation
- `USAGE.md` - Usage examples
- `EXAMPLES.md` - Real-world examples
- `example-config.jsonc` - Example configuration

## Pull Request Process

1. Ensure all tests pass
2. Update documentation as needed
3. Follow the existing code style
4. Provide a clear description of changes
5. Reference any related issues

## Feature Ideas

Here are some ideas for contributions:

- [ ] Add support for more system information fields
- [ ] Improve animated GIF rendering
- [ ] Add themes/color schemes
- [ ] Support for additional image formats
- [ ] Plugin system for custom info sources
- [ ] Network information display
- [ ] GPU information support
- [ ] Custom ASCII art support
- [ ] Configuration validation
- [ ] More interactive features

## Bug Reports

When reporting bugs, please include:

1. Python version: `python --version`
2. Operating system and version
3. AnimatedFetching version
4. Steps to reproduce
5. Expected vs actual behavior
6. Any error messages or logs

## Questions and Support

- Open an issue for questions
- Check existing issues before creating new ones
- Be respectful and constructive

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help create a positive community

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Acknowledgments

Thank you to all contributors who help make AnimatedFetching better!
