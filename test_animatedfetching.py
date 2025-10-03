#!/usr/bin/env python3
"""
Basic tests for AnimatedFetching
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from animatedfetching.sysinfo import SystemInfo
from animatedfetching.config import Config
from animatedfetching.main import AnimatedFetching


def test_sysinfo():
    """Test system information gathering"""
    print("Testing SystemInfo...")
    
    info = SystemInfo.get_all()
    
    # Check all required keys are present
    required_keys = ['hostname', 'os', 'kernel', 'uptime', 'shell', 'terminal', 'cpu', 'memory', 'disk']
    for key in required_keys:
        assert key in info, f"Missing key: {key}"
        assert info[key], f"Empty value for key: {key}"
    
    print("✓ SystemInfo test passed")
    return True


def test_config():
    """Test configuration loading"""
    print("Testing Config...")
    
    # Test default config
    config = Config.load()
    assert 'animation' in config
    assert 'info_sections' in config
    assert 'buttons' in config
    assert 'layout' in config
    assert 'colors' in config
    
    # Test config structure
    assert isinstance(config['info_sections'], list)
    assert isinstance(config['buttons'], list)
    assert isinstance(config['layout'], dict)
    
    print("✓ Config test passed")
    return True


def test_app_initialization():
    """Test application initialization"""
    print("Testing AnimatedFetching initialization...")
    
    try:
        app = AnimatedFetching()
        assert app.config is not None
        assert app.sysinfo is not None
        assert app.console is not None
        print("✓ App initialization test passed")
        return True
    except Exception as e:
        print(f"✗ App initialization test failed: {e}")
        return False


def test_display():
    """Test display rendering"""
    print("Testing display rendering...")
    
    try:
        app = AnimatedFetching()
        
        # Test info section rendering
        info_table = app.render_info_section()
        assert info_table is not None
        
        # Test buttons rendering
        buttons_panel = app.render_buttons()
        assert buttons_panel is not None
        
        print("✓ Display rendering test passed")
        return True
    except Exception as e:
        print(f"✗ Display rendering test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("Running AnimatedFetching Tests")
    print("=" * 60)
    print()
    
    tests = [
        test_sysinfo,
        test_config,
        test_app_initialization,
        test_display,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
            results.append(False)
        print()
    
    print("=" * 60)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    if all(results):
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
