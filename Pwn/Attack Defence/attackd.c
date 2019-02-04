//gcc attackd.c -o test -no-pie -fno-pic -mpreferred-stack-boundary=3 -fno-stack-protector

#include <stdio.h>
#include <unistd.h>

int initialize()
{
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

void main()
{
  char buf[0x10]={0};
  initialize();
  puts("Super awesome server\n Give input and enjoy the seashell\n");
  read(0,buf,0x100);
}
