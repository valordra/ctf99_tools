#include <stdio.h>
#include <stdlib.h>

void target(int p1) {
    FILE *f = fopen("flag.txt","r");
    if (p1 == 0x12345678) {
        char flag[100];
        fgets(flag, 100, f);
        puts(flag);
    }
}

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
