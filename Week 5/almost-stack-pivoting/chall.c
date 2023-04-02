#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void vuln() {
    char buf[8];
    scanf("%32s", buf);
}

void leak() {
	int x;
	printf("address for you: %lx\n", &x);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    leak();
    vuln();
}