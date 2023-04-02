#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    
    char buf[16];
    printf("Address: %p\n", &buf);

    printf("Shellcode: ");
    gets(buf);

    int find_0f = 0;
    for (int i = 0; i < strlen(buf); i++) {
        if (buf[i] == '\x0f') {
            find_0f = 1;
            continue;
        } else if (buf[i] == '\x05') {
            if (find_0f == 1) {
                printf("no syscall.");
                exit(0);
            }
        }
        find_0f = 0;
    }
}