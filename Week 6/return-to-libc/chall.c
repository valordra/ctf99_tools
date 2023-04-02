#define _GNU_SOURCE     /* for RTLD_NEXT */
#include<dlfcn.h>
#include<stdio.h>
#include<stdlib.h>

char *str = "/bin/sh";

void vuln() {
    char buf[8];
    gets(buf);
}

void init()	{
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
    init();
    printf("string /bin/sh: %p\n", str);
    printf("puts: %p\n", dlsym(RTLD_NEXT, "puts"));
    vuln();
    return 0;
}
