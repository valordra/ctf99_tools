
undefined8 main(void)

{
  int iVar1;
  char local_88 [56];
  undefined8 local_50;
  char local_48 [8];
  char acStack_40 [8];
  undefined local_38;
  undefined local_37;
  undefined local_36;
  undefined local_35;
  char acStack_34 [4];
  char acStack_30 [40];
  
  local_50 = 0x3234303645435343;
  strcpy(local_48,(char *)&local_50);
  local_50 = 0x6169646e657b3835;
  strcpy(acStack_40,(char *)&local_50);
  local_38 = 0x6e;
  local_37 = 0x6e;
  local_36 = 0x65;
  local_35 = 0x73;
  local_50 = 0x616d5f73;
  strcpy(acStack_34,(char *)&local_50);
  local_50 = 0x7d7372657474;
  strcpy(acStack_30,(char *)&local_50);
  printf("Flag: ");
  __isoc99_scanf(&DAT_0010098b,local_88);
  iVar1 = strcmp(local_48,local_88);
  if (iVar1 == 0) {
    puts("Correct.");
  }
  else {
    puts("Wrong.");
  }
  return 0;
}

