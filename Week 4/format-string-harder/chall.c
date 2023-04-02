#include <stdio.h>
#include <stdlib.h>

char notFlag[13] = "not-flag.txt\0";

void target() {
    char flag[64];
    FILE *f = fopen(notFlag,"r");
    fgets(flag,64,f);
    puts(flag);
}

int vuln() {
    char buf[66];
	printf("> ");
    scanf("%64s", buf);
    printf(buf);
}

void leak() {
	int x;
	printf("address for you: %lx\n", &x);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
	leak();
    vuln();
    return 0;
}
