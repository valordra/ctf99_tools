#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdlib.h>

char notFlag[13] = "not-flag.txt\0";
int canary1;
int canary2;
int canary3;


void initialize(){
    srand(time(NULL));   // Initialization, should only be called once.
    canary1 = rand();
    canary2 = rand();
    canary3 = rand();
}
void printvar(char var_name, int value){
    printf("%c:  %d\n", var_name, value);
}

struct Variables{
    char input[44];
    int can1;
    int a;
    int b;
    int can2;
    int c;
    int d; 
    int e;
    int can3;
};


// -fno-toplevel-reorder
int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    initialize();
    
    struct Variables v;
    v.can1 = canary1;
    v.a=0;
    v.b=1;
    v.can2 = canary2;
    v.c=2;
    v.d=3; 
    v.e=4;
    v.can3 = canary3;
    
    
    
    printf("Hello! Please give your input:\n");
    scanf("%s", v.input);
    printf("Your input: \n");
    printf(v.input, &v.a, &v.b, &v.c, &v.d, &v.e);
    printf("\n");
    
    if (v.can3 != canary3){
        puts("Canary3 stack smashing detected");
        exit(1);
    }
    if (v.can2 != canary2){
        puts("Canary2 stack smashing detected");
        exit(1);
    }
    if (v.can1 != canary1){
        puts("Canary1 stack smashing detected");
        exit(1);
    }
    
    
    puts("");
    if (v.a==45 && v.b==30 && v.c==46 && v.d==10 && v.e==15){
        puts("You win!");
        system("echo \"Here is your flag\"; cat flag.txt");
        puts("\n");
    }else{
        puts("variables: ");
        printvar('a', v.a);
        printvar('b', v.b);
        printvar('c', v.c);
        printvar('d', v.d);
        printvar('e', v.e);
        puts("Bye!");
    }
    return 0;
}
