#include <stdio.h>
#include <stdlib.h>

FILE* fp;
char* flag;

void target(int p1, int p2) {
    if (p1 == 0x12345678 && p2 == 0x87654321) {
        puts("flag opened.");
        fp = fopen("flag.txt","r");
    } else if (p1 == 0x11223344 && p2 == 0x44332211) {
        puts("flag read.");
        fgets(flag, 100, fp);
    } else if (p1 == 0x41414141 && p2 == 0x42424242) {
        puts(flag);
    }
}

void vuln() {
    char buf[8];
    puts("good luck!");
    gets(buf);
}

void init()	{
    // Don't call this function more than once!
    setvbuf(stdout, NULL, _IONBF, 0);
    flag = malloc(200);
}

int main() {
    init();
    vuln();
    return 0;
}
