#include <stdio.h>

void onegaishimasu() {
    char flag[64];
    FILE *f = fopen("flag.txt","r");
    fgets(flag,64,f);
    puts(flag);
}

void leak() {
    int nanikore;
    printf("Oh no! Did you just leak me? :scream: %p %p\n", leak, &nanikore);
}

void vuln() {
    char buf[64];
    printf("Konnichiwa, this is a classic buffer overflow challenge ^^\nどうぞ : ");
    gets(buf);
}

void main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    while(1) {
        printf("1. Leak\n2. Overflow\n> ");

        int nani;
        scanf("%d", &nani);
        if (nani == 1) {
            leak();
        } else if (nani == 2) {
            getchar();
            vuln();
        } else {
            printf("もうぉぉ〜ご主人様は悪い子ですね〜〜〜 (>//<)\n");
            break;
        }
    }
}

// gcc -fno-stack-protector -o chall chall.c
