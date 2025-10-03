#!/bin/bash
# Simple test script for AnimatedFetching

set -e

echo "Running AnimatedFetching tests..."
echo ""

# Test 1: Build
echo "Test 1: Building..."
make clean > /dev/null
make > /dev/null
if [ -f "bin/afetch" ]; then
    echo "✓ Build successful"
else
    echo "✗ Build failed"
    exit 1
fi

# Test 2: Help output
echo "Test 2: Help output..."
if ./bin/afetch --help | grep -q "AnimatedFetching"; then
    echo "✓ Help output working"
else
    echo "✗ Help output failed"
    exit 1
fi

# Test 3: Run without GIF
echo "Test 3: Run without GIF..."
# This should run and display info even without a GIF
if ./bin/afetch --gif /nonexistent/file.gif 2>&1 | grep -q "Warning: GIF file not found"; then
    echo "✓ Graceful fallback working"
else
    echo "✗ Fallback failed"
    exit 1
fi

# Test 4: Run with GIF (if available)
if [ -f "animatedfetching/resources/default_animation.gif" ]; then
    echo "Test 4: Run with GIF..."
    if ./bin/afetch --gif animatedfetching/resources/default_animation.gif 2>&1 | grep -q "Kernel"; then
        echo "✓ GIF rendering and info display working"
    else
        echo "✗ GIF rendering failed"
        exit 1
    fi
else
    echo "Test 4: Skipped (no GIF available)"
fi

# Test 5: Output contains expected info
echo "Test 5: System info gathering..."
OUTPUT=$(./bin/afetch --gif /nonexistent/file.gif 2>&1)
CHECKS=("OS" "Kernel" "Uptime" "Shell" "Terminal" "CPU" "Memory")
for check in "${CHECKS[@]}"; do
    if echo "$OUTPUT" | grep -q "$check"; then
        echo "  ✓ $check found"
    else
        echo "  ✗ $check missing"
        exit 1
    fi
done

echo ""
echo "All tests passed! ✓"
