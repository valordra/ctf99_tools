#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    char buff[256];
    fgets(buff, 1024, stdin);
    if (strlen(buff)<11)
        printf(buff);
    exit(0);
}
