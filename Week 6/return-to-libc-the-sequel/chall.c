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
    puts("good luck!");
    vuln();
    return 0;
}
