#include "animatedfetch.h"
#include <sys/ioctl.h>
#include <time.h>

void get_hostname(char *hostname) {
    if (gethostname(hostname, MAX_LINE_LENGTH) != 0) {
        strcpy(hostname, "unknown");
    }
}

void get_os(char *os) {
    FILE *fp = fopen("/etc/os-release", "r");
    if (fp) {
        char line[MAX_LINE_LENGTH];
        
        while (fgets(line, sizeof(line), fp)) {
            if (strncmp(line, "PRETTY_NAME=", 12) == 0) {
                // Extract value between quotes
                char *start = strchr(line, '"');
                if (start) {
                    start++;
                    char *end = strchr(start, '"');
                    if (end) {
                        *end = '\0';
                        strncpy(os, start, MAX_LINE_LENGTH - 1);
                        fclose(fp);
                        return;
                    }
                }
            }
        }
        fclose(fp);
    }
    
    // Fallback
    struct utsname uts;
    if (uname(&uts) == 0) {
        snprintf(os, MAX_LINE_LENGTH, "%s", uts.sysname);
    } else {
        strcpy(os, "Unknown");
    }
}

void get_kernel(char *kernel) {
    struct utsname uts;
    if (uname(&uts) == 0) {
        snprintf(kernel, MAX_LINE_LENGTH, "%s", uts.release);
    } else {
        strcpy(kernel, "Unknown");
    }
}

void get_uptime(char *uptime) {
    struct sysinfo info;
    if (sysinfo(&info) == 0) {
        long uptime_secs = info.uptime;
        int days = uptime_secs / 86400;
        int hours = (uptime_secs % 86400) / 3600;
        int minutes = (uptime_secs % 3600) / 60;
        
        if (days > 0) {
            snprintf(uptime, MAX_LINE_LENGTH, "%dd %dh %dm", days, hours, minutes);
        } else if (hours > 0) {
            snprintf(uptime, MAX_LINE_LENGTH, "%dh %dm", hours, minutes);
        } else {
            snprintf(uptime, MAX_LINE_LENGTH, "%dm", minutes);
        }
    } else {
        strcpy(uptime, "Unknown");
    }
}

void get_shell(char *shell) {
    char *shell_env = getenv("SHELL");
    if (shell_env) {
        char *shell_name = strrchr(shell_env, '/');
        if (shell_name) {
            strncpy(shell, shell_name + 1, MAX_LINE_LENGTH - 1);
        } else {
            strncpy(shell, shell_env, MAX_LINE_LENGTH - 1);
        }
    } else {
        strcpy(shell, "unknown");
    }
}

void get_terminal(char *terminal) {
    char *term_env = getenv("TERM");
    if (term_env) {
        strncpy(terminal, term_env, MAX_LINE_LENGTH - 1);
    } else {
        strcpy(terminal, "unknown");
    }
}

void get_cpu(char *cpu) {
    FILE *fp = fopen("/proc/cpuinfo", "r");
    if (fp) {
        char line[MAX_LINE_LENGTH];
        while (fgets(line, sizeof(line), fp)) {
            if (strncmp(line, "model name", 10) == 0) {
                char *colon = strchr(line, ':');
                if (colon) {
                    colon += 2; // Skip ": "
                    // Remove newline
                    char *newline = strchr(colon, '\n');
                    if (newline) *newline = '\0';
                    strncpy(cpu, colon, MAX_LINE_LENGTH - 1);
                    fclose(fp);
                    return;
                }
            }
        }
        fclose(fp);
    }
    strcpy(cpu, "Unknown CPU");
}

void get_memory(char *memory) {
    struct sysinfo info;
    if (sysinfo(&info) == 0) {
        unsigned long total_mb = info.totalram / 1024 / 1024;
        unsigned long used_mb = (info.totalram - info.freeram) / 1024 / 1024;
        unsigned long total_gb = total_mb / 1024;
        
        if (total_gb > 0) {
            snprintf(memory, MAX_LINE_LENGTH, "%.1fGB / %.1fGB", 
                     used_mb / 1024.0, total_mb / 1024.0);
        } else {
            snprintf(memory, MAX_LINE_LENGTH, "%luMB / %luMB", used_mb, total_mb);
        }
    } else {
        strcpy(memory, "Unknown");
    }
}

void get_system_info(SystemInfo *info) {
    get_hostname(info->hostname);
    get_os(info->os);
    get_kernel(info->kernel);
    get_uptime(info->uptime);
    get_shell(info->shell);
    get_terminal(info->terminal);
    get_cpu(info->cpu);
    get_memory(info->memory);
}

int get_terminal_width() {
    struct winsize w;
    if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &w) == 0) {
        return w.ws_col;
    }
    return 80; // Default fallback
}

void print_centered(const char *text, int term_width) {
    int text_len = strlen(text);
    int padding = (term_width - text_len) / 2;
    if (padding > 0) {
        for (int i = 0; i < padding; i++) {
            printf(" ");
        }
    }
    printf("%s\n", text);
}
