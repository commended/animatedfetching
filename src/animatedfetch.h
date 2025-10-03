#ifndef ANIMATEDFETCH_H
#define ANIMATEDFETCH_H

#define _POSIX_C_SOURCE 200112L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/utsname.h>
#include <sys/sysinfo.h>
#include <pwd.h>
#include <gif_lib.h>

#define MAX_LINE_LENGTH 256
#define MAX_INFO_LINES 20

// System information structure
typedef struct {
    char hostname[MAX_LINE_LENGTH];
    char os[MAX_LINE_LENGTH];
    char kernel[MAX_LINE_LENGTH];
    char uptime[MAX_LINE_LENGTH];
    char shell[MAX_LINE_LENGTH];
    char terminal[MAX_LINE_LENGTH];
    char cpu[MAX_LINE_LENGTH];
    char memory[MAX_LINE_LENGTH];
} SystemInfo;

// GIF frame data
typedef struct {
    int width;
    int height;
    unsigned char *data;  // RGB data
} GIFFrame;

// Function declarations
void get_system_info(SystemInfo *info);
void get_hostname(char *hostname);
void get_os(char *os);
void get_kernel(char *kernel);
void get_uptime(char *uptime);
void get_shell(char *shell);
void get_terminal(char *terminal);
void get_cpu(char *cpu);
void get_memory(char *memory);

int load_gif(const char *filename, GIFFrame *frame);
void render_gif_frame(GIFFrame *frame, int term_width);
void render_info(SystemInfo *info, int term_width);
void free_gif_frame(GIFFrame *frame);

int get_terminal_width();
void print_centered(const char *text, int term_width);

#endif // ANIMATEDFETCH_H
