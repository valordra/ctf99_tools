#include <stdio.h>
#include <stdlib.h>

void target() {
	char flag[64];
    FILE *f = fopen("flag.txt","r");
    fgets(flag,64,f);
	puts(flag);
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

int n;
double sum = 0.0;

int main(int argc, char const *argv[]) {
	init();

	puts("How many times?");
	scanf("%d", &n);

	double ar[4];
	for (int i = 0; i < n; i++) {
		scanf("%lf", &ar[i]);
		sum += ar[i];
	}
	printf("Result: %a\n\n", sum);

	char buf[10];
	puts("Say something:");
	scanf("%s", buf);
	puts("Bye.");
}
