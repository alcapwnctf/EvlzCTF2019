#include<stdio.h>
#include<stdlib.h>

int main(){
        FILE *fp=NULL;
        int i=0, len;
        unsigned char *ch;
        printf("Reading file...\n");
        fp = fopen("jpg.JPG", "rb");
        //fgets(ch, 51, fp);
        fseek(fp, 0, SEEK_END);
        //len = ftell(fp);
        len = 100;
        printf("Len: %d\n", len);
        fseek(fp, 0, SEEK_SET);
        ch = (unsigned char*)malloc(len);
        printf("Assigned memory.\n");
        fread(ch, len, sizeof(unsigned char), fp);
        printf("File read.\n");
        printf("    %c\n",ch[0]);
        printf("%s", ch);
        fclose(fp);
        return 0;
}
