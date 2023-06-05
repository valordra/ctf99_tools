#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>

#define BUFSIZE 16

bool a = false;
bool b = false;


void f1(unsigned int a1) {
  if (a1 == 0xDEADBEEF)
  a = true;
}

void f2(unsigned int a2) {
  if (a && a2 == 0xBAAAAAAD) {
    b = true;
  }
  else if (a) {
    printf("Wrong Argument.\n");
  }
  else {
    printf("Nope.\n");
  }
}

void f3(unsigned int a3, unsigned int a4) {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  
  if (a && b && a3 == 0xDEADBAAD && a4 == 0xDEEEAAAD) {
    printf("%s", flag);
    return;
  }
  else if (a && b) {
    printf("Incorrect Argument. \n");
  }
  else if (a || b) {
    printf("Nice Try! \n");
  }
  else {
    printf("Sorry..\n");
  }
}

void vuln() {
  char buf[24];
  printf("Enter input: ");
  return gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
}

//gcc -m32 -fno-stack-protector -no-pie chall.c -o chall
