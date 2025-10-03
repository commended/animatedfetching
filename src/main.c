#include "animatedfetch.h"

void print_usage(const char *prog_name) {
    printf("Usage: %s [OPTIONS]\n", prog_name);
    printf("\nAnimatedFetching - A terminal fetch program with GIF support\n");
    printf("\nOptions:\n");
    printf("  -g, --gif <path>    Path to GIF file (default: ~/.config/animatedfetching/animation.gif)\n");
    printf("  -h, --help          Show this help message\n");
    printf("\n");
}

int main(int argc, char *argv[]) {
    char gif_path[512];
    char *home = getenv("HOME");
    
    // Default GIF path
    if (home) {
        snprintf(gif_path, sizeof(gif_path), "%s/.config/animatedfetching/animation.gif", home);
    } else {
        strcpy(gif_path, "animation.gif");
    }
    
    // Parse command line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_usage(argv[0]);
            return 0;
        } else if ((strcmp(argv[i], "-g") == 0 || strcmp(argv[i], "--gif") == 0) && i + 1 < argc) {
            strncpy(gif_path, argv[++i], sizeof(gif_path) - 1);
        }
    }
    
    // Get terminal width
    int term_width = get_terminal_width();
    
    // Clear screen and move cursor to top
    printf("\033[2J\033[H");
    
    // Add top padding
    printf("\n\n");
    
    // Load and render GIF if it exists
    GIFFrame frame = {0};
    if (access(gif_path, F_OK) == 0) {
        if (load_gif(gif_path, &frame) == 0) {
            render_gif_frame(&frame, term_width);
        } else {
            fprintf(stderr, "Warning: Failed to load GIF from %s\n", gif_path);
        }
    } else {
        fprintf(stderr, "Warning: GIF file not found at %s\n", gif_path);
        fprintf(stderr, "Continuing without animation...\n");
    }
    
    // Get system information
    SystemInfo info;
    get_system_info(&info);
    
    // Render system info
    render_info(&info, term_width);
    
    // Cleanup
    free_gif_frame(&frame);
    
    return 0;
}
