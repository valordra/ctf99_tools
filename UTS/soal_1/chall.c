# include <stdio.h>
# include <stdlib.h>
# include <string.h>

void input()
{
    char buf[100];
    gets(buf);
}

void b()
{
    char b[64];
    FILE *f = fopen("flag.txt","r");
    fgets(b,64,f);
    puts(b);
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("Enter your input:\n");
    input();
    return 0;
}

//gcc -fno-stack-protector -no-pie -o chall chall.c
