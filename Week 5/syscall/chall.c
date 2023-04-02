#include<stdio.h>
#include<sys/syscall.h>
#include<unistd.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    long args[8];
    char s[1005];
    printf("Address: %p\n", &s);

    while(1) {
        printf("> ");
        scanf("%1000s", s);
        
        for (int i = 0; i < 7; i++) {
            printf("arg[%d]: ", i);
            scanf("%ld", &args[i]);
        }
        printf("syscall(%ld, %ld, %ld, %ld, %ld, %ld, %ld)\n", args[0], args[1], args[2], args[3], args[4], args[5], args[6]);
        syscall(args[0], args[1], args[2], args[3], args[4], args[5], args[6]);
    }
}