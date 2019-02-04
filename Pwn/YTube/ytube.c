#gcc lol.c -o hack -m32 -no-pie

#include <stdio.h>

void win(char *comm){
	system(comm);
}

int buff[512];
int main(int argc, char **argv){
	while(1){
		fgets(buff, 512, stdin);
		printf(buff);
	}
	return 0;
}
