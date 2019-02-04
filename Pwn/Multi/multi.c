//gcc multi.c -o multi -lpthread -no-pie

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<pthread.h> 

int maxval = 10000;
int choice;
int stage1status=0,stage2status=0,stage3status=0;

void initialize(){
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

int stage1(){
  printf("Solve this challenge to advance\nEnter two numbers: ");
  unsigned int a,b;

  scanf("%d %d",&a,&b);
  if (((int)a>1336)||((int)b>1336))return 0;
  while((getchar())!='\n');
  if (b-a==1337){
    stage1status=1;
    return 1;
    }
  else return 0;
}

int subnumber(){
  int n;
  printf("Enter a number between 1-250 inclusive: ");
  scanf("%d",&n);
  getchar();
  if (1<=n && n<=250){
    maxval-=n;
    return 1;
  }
  else return 0;
}

int addnumber(){
  int n;
  printf("Enter a number between 1-250 inclusive: ");
  scanf("%d",&n);
  getchar();
  
  int maxupdate=10000-maxval;
  if (1<=n && n<=250){
    if (n > maxupdate){
      n=maxupdate;
    } 
    maxval+=n; 
    return 1;
  }
  else return 0;
}

void* check(){
  while(maxval<=10000){
    if (maxval < 5000){
    sleep(4);
    maxval+=4900;
    }
  } 
}

void* operations(){
  while(maxval>0){
    printf("1. Add a number between 0-250\n");
    printf("2. Subtract a number between 0-250\n>> ");
    int ch;
    scanf("%d",&ch);
    getchar();
    switch (ch){
    case 1:
      addnumber();
      printf("Val is now %d\n",maxval);
      sleep(1);
      break;
    case 2:
      subnumber();
      printf("Val is now %d\n",maxval);
      sleep(1);
      break;
    default:
      exit(0);
    }
  }
}
  

int stage2(){
  pthread_t thread_operations, thread_check;  
  pthread_create(&thread_operations, NULL, operations, NULL); 
  pthread_create(&thread_check, NULL, check, NULL); 
  pthread_join(thread_operations, NULL);
  if (maxval<0){
    stage2status=1;
    return 1;
    }
  else return 0;
}

int stage3(){
  char description[200];
  unsigned long address, Gaddress;

  puts("Now that you are here, you gotta tell me about yourself: ");
  fgets(description,sizeof(description),stdin);
  char *end = strchr(description, '\n');
  if (end != NULL)*end = '\x00';
  
  printf("So you say that you are a \n\t");
  printf(description);
  puts("\nOkay, let's see how good you are\nGive me the address of the puts function");
  scanf("%lu",&Gaddress);
  getchar();
  address=puts;
  if (address==Gaddress){
    stage3status=1;
    return 1;
  }
  else return 0;
}
void exitp(){
  exit(1);
}

int finish(){
  if (stage1status && stage2status && stage3status)
  {
    system("/bin/sh");
    return 0;
  }
  else
  {
    exit(1);
  }
  
}

void stage4(){
  puts("We are about to finish. I hope you had fun");
  //int ch;
  unsigned long* memaddr=0, captcha=0;
  int addr=0;

  while(1){
    printf("1. Create a memory region\n");
    printf("2. Delete the memory region\n");
    printf("3. Do some captcha\n");
    printf("4. Jump\n");
    printf(">>");
    scanf("%d",&choice);
    getchar();
    switch (choice)
    {
      case 1:
        memaddr=(unsigned long)malloc(sizeof(unsigned long));
        *memaddr=exitp;
        addr=1;
        break;

      case 2:
        free(memaddr);
        break;

      case 3:
        captcha=(unsigned long) malloc(sizeof(unsigned long));
        printf("Whats the sum of 0xdeadbeef and 0xcafebabe: ");
        scanf("%lu",captcha);
        getchar();
        
        break;

      case 4:
        if(!addr)exit(1);
        int(*jopme)()=(int(*)())*memaddr;
        jopme();
        break;
    
      default:
        exit(1);
        break;
    }
  }
  return;
}

int main(){
  initialize();
  
  if (stage1()){
    if (stage2()){
      if (stage3()){
           stage4();
      }
      else puts("Go learn some more\n");
    }
    else puts("Go learn some more\n");
  }
  else puts("Go learn some more\n");

  return 0;
}