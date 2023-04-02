#include <stdio.h>
#include <stdlib.h>

FILE* fp;
char* flag;

void target(long p1, long p2) {
    if (p1 == 0x1234567812345678 && p2 == 0x8765432187654321) {
        puts("flag opened.");
        fp = fopen("flag.txt","r");
    } else if (p1 == 0x1122334455667788 && p2 == 0x8877665544332211) {
        puts("flag read.");
        fgets(flag, 100, fp);
    } else if (p1 == 0x4141414142424242 && p2 == 0x4343434344444444) {
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
