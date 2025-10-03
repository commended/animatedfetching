CC = gcc
CFLAGS = -Wall -Wextra -O2 -std=c11
LDFLAGS = -lgif

SRC_DIR = src
BUILD_DIR = build
BIN_DIR = bin

SOURCES = $(SRC_DIR)/main.c $(SRC_DIR)/sysinfo.c $(SRC_DIR)/render.c
OBJECTS = $(SOURCES:$(SRC_DIR)/%.c=$(BUILD_DIR)/%.o)
TARGET = $(BIN_DIR)/afetch

PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin

.PHONY: all clean install uninstall

all: $(TARGET)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS) | $(BIN_DIR)
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@
	@echo "Build complete! Binary: $(TARGET)"

clean:
	rm -rf $(BUILD_DIR) $(BIN_DIR)

install: $(TARGET)
	install -D -m 755 $(TARGET) $(DESTDIR)$(BINDIR)/afetch
	@echo "Installed to $(DESTDIR)$(BINDIR)/afetch"

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/afetch
	@echo "Uninstalled from $(DESTDIR)$(BINDIR)/afetch"

help:
	@echo "AnimatedFetching - Makefile targets:"
	@echo "  all       - Build the program (default)"
	@echo "  clean     - Remove build artifacts"
	@echo "  install   - Install to $(PREFIX)/bin"
	@echo "  uninstall - Remove from $(PREFIX)/bin"
	@echo "  help      - Show this help message"
