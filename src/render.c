#include "animatedfetch.h"

// ANSI color codes for 24-bit RGB
void set_rgb_color(unsigned char r, unsigned char g, unsigned char b) {
    printf("\033[38;2;%d;%d;%dm", r, g, b);
}

void reset_color() {
    printf("\033[0m");
}

int load_gif(const char *filename, GIFFrame *frame) {
    int error;
    GifFileType *gif = DGifOpenFileName(filename, &error);
    
    if (!gif) {
        fprintf(stderr, "Failed to open GIF file: %s\n", filename);
        return -1;
    }
    
    // Read the GIF data
    if (DGifSlurp(gif) == GIF_ERROR) {
        fprintf(stderr, "Failed to read GIF data\n");
        DGifCloseFile(gif, &error);
        return -1;
    }
    
    if (gif->ImageCount == 0) {
        fprintf(stderr, "GIF has no images\n");
        DGifCloseFile(gif, &error);
        return -1;
    }
    
    // Get the first frame
    SavedImage *image = &gif->SavedImages[0];
    frame->width = image->ImageDesc.Width;
    frame->height = image->ImageDesc.Height;
    
    // Allocate RGB data
    frame->data = malloc(frame->width * frame->height * 3);
    if (!frame->data) {
        DGifCloseFile(gif, &error);
        return -1;
    }
    
    // Get the color map
    ColorMapObject *colorMap = image->ImageDesc.ColorMap ? 
                               image->ImageDesc.ColorMap : 
                               gif->SColorMap;
    
    if (!colorMap) {
        fprintf(stderr, "No color map in GIF\n");
        free(frame->data);
        DGifCloseFile(gif, &error);
        return -1;
    }
    
    // Convert indexed color to RGB
    for (int i = 0; i < frame->width * frame->height; i++) {
        int colorIndex = image->RasterBits[i];
        if (colorIndex >= colorMap->ColorCount) {
            colorIndex = 0;
        }
        GifColorType color = colorMap->Colors[colorIndex];
        frame->data[i * 3] = color.Red;
        frame->data[i * 3 + 1] = color.Green;
        frame->data[i * 3 + 2] = color.Blue;
    }
    
    DGifCloseFile(gif, &error);
    return 0;
}

void render_gif_frame(GIFFrame *frame, int term_width) {
    if (!frame || !frame->data) {
        return;
    }
    
    // Scale down the frame to fit terminal width (max 40 characters)
    int display_width = frame->width;
    if (display_width > 40) {
        display_width = 40;
    }
    
    // Calculate aspect ratio adjustment for terminal characters
    // (characters are typically taller than they are wide)
    int display_height = (frame->height * display_width) / frame->width / 2;
    
    // Render each line centered
    for (int y = 0; y < display_height; y++) {
        // Calculate source y position
        int src_y = (y * frame->height * 2) / display_height;
        if (src_y >= frame->height) src_y = frame->height - 1;
        
        // Calculate padding for centering
        int padding = (term_width - display_width) / 2;
        for (int i = 0; i < padding; i++) {
            printf(" ");
        }
        
        // Render each pixel as a colored block character
        for (int x = 0; x < display_width; x++) {
            int src_x = (x * frame->width) / display_width;
            if (src_x >= frame->width) src_x = frame->width - 1;
            
            int idx = (src_y * frame->width + src_x) * 3;
            unsigned char r = frame->data[idx];
            unsigned char g = frame->data[idx + 1];
            unsigned char b = frame->data[idx + 2];
            
            set_rgb_color(r, g, b);
            printf("█");
        }
        
        reset_color();
        printf("\n");
    }
}

void render_info(SystemInfo *info, int term_width) {
    char line[512]; // Increase buffer size to avoid truncation
    
    // Print a blank line for spacing
    printf("\n");
    
    // Print hostname with color
    snprintf(line, sizeof(line), "\033[1;36m%s\033[0m", info->hostname);
    print_centered(line, term_width);
    
    // Print separator (using simple dash instead of Unicode)
    char separator[81];
    memset(separator, '-', 40);
    separator[40] = '\0';
    print_centered(separator, term_width);
    
    // Print system info
    struct {
        const char *label;
        const char *value;
        const char *color;
    } fields[] = {
        {"OS", info->os, "36"},         // cyan
        {"Kernel", info->kernel, "34"}, // blue
        {"Uptime", info->uptime, "32"}, // green
        {"Shell", info->shell, "33"},   // yellow
        {"Terminal", info->terminal, "35"}, // magenta
        {"CPU", info->cpu, "31"},       // red
        {"Memory", info->memory, "36"}, // cyan
    };
    
    for (int i = 0; i < 7; i++) {
        snprintf(line, sizeof(line), "\033[1;%sm%-10s\033[0m %s", 
                 fields[i].color, fields[i].label, fields[i].value);
        print_centered(line, term_width);
    }
    
    printf("\n");
}

void free_gif_frame(GIFFrame *frame) {
    if (frame && frame->data) {
        free(frame->data);
        frame->data = NULL;
    }
}
