#include<stdio.h>
#include<stdlib.h>

void vuln() {
    char buf[8];
    gets(buf);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    puts("good luck!");
    vuln();
    return 0;
}