#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>


/*
(100, 79, 58, 24, 42, 9, 37, 72)
(6, 48, 33, 11, 52, 54, 53, 63)
(49, 94, 20, 76, 36, 4, 43, 51)
(17, 95, 32, 13, 31, 84, 68, 1)
(30, 83, 21, 85, 87, 12, 2, 39)
(7, 5, 29, 92, 77, 96, 99, 67)
(57, 22, 45, 78, 73, 46, 19, 16)
*/

char graph[101][101];
char flag[100];
int idx=0;

void initialize(){
    memset(graph,'~',sizeof(graph));
    graph[79][57]='7';
    graph[85][13]='W';
    graph[33][58]='W';
    graph[19][72]='F';
    graph[85][77]='6';
    graph[77][87]='I';
    graph[45][78]='f';
    graph[76][11]='j';
    graph[45][29]='{';
    graph[11][33]='s';
    graph[84][12]='W';
    graph[19][37]='O';
    graph[54][42]='W';
    graph[5][7]='1';
    graph[24][78]='N';
    graph[73][42]='c';
    graph[87][31]='6';
    graph[54][53]='P';
    graph[42][54]='W';
    graph[11][24]='X';
    graph[37][46]='e';
    graph[78][42]='7';
    graph[33][48]='u';
    graph[45][24]='e';
    graph[51][53]='a';
    graph[46][9]='c';
    graph[49][6]='}';
    graph[46][96]='j';
    graph[67][99]='_';
    graph[11][36]='G';
    graph[78][45]='f';
    graph[43][51]='m';
    graph[92][73]='8';
    graph[17][30]='t';
    graph[17][49]='E';
    graph[77][92]='_';
    graph[57][22]='c';
    graph[6][100]='A';
    graph[2][12]='s';
    graph[2][99]='F';
    graph[24][42]='z';
    graph[30][83]='3';
    graph[48][94]='e';
    graph[20][48]='7';
    graph[100][48]='o';
    graph[79][33]='2';
    graph[57][100]='z';
    graph[43][4]='0';
    graph[22][57]='c';
    graph[53][54]='P';
    graph[37][19]='O';
    graph[20][76]='4';
    graph[7][22]='v';
    graph[19][99]='o';
    graph[7][5]='1';
    graph[9][42]='{';
    graph[92][78]='X';
    graph[42][9]='{';
    graph[39][68]='C';
    graph[94][48]='e';
    graph[76][36]='_';
    graph[19][16]='f';
    graph[5][29]='0';
    graph[22][79]='z';
    graph[19][46]='t';
    graph[63][37]='r';
    graph[51][43]='m';
    graph[78][24]='N';
    graph[99][67]='_';
    graph[4][36]='c';
    graph[49][17]='E';
    graph[21][92]='Q';
    graph[84][36]='Y';
    graph[96][77]='i';
    graph[87][85]='u';
    graph[11][58]='m';
    graph[76][13]='m';
    graph[19][96]='r';
    graph[52][24]='l';
    graph[76][31]='e';
    graph[83][17]='s';
    graph[43][53]='P';
    graph[11][52]='7';
    graph[1][43]='v';
    graph[54][52]='_';
    graph[92][29]='n';
    graph[84][31]='t';
    graph[21][83]='_';
    graph[54][4]='N';
    graph[32][13]='t';
    graph[31][36]='2';
    graph[12][31]='w';
    graph[43][68]='Z';
    graph[22][45]='T';
    graph[92][77]='_';
    graph[53][37]='h';
    graph[2][67]='A';
    graph[76][20]='4';
    graph[43][54]='Y';
    graph[5][22]='n';
    graph[68][4]='l';
    graph[22][5]='n';
    graph[84][68]='1';
    graph[30][17]='t';
    graph[94][6]='B';
    graph[13][20]='N';
    graph[6][94]='B';
    graph[46][73]='c';
    graph[31][87]='6';
    graph[94][49]='t';
    graph[16][99]='Y';
    graph[24][52]='l';
    graph[45][5]='Y';
    graph[63][53]='u';
    graph[7][57]='8';
    graph[68][39]='C';
    graph[33][20]='D';
    graph[2][39]='t';
    graph[33][76]='X';
    graph[48][79]='S';
    graph[22][7]='v';
    graph[95][94]='Y';
    graph[72][37]='_';
    graph[9][73]='2';
    graph[73][9]='2';
    graph[87][12]='3';
    graph[42][78]='7';
    graph[6][48]='J';
    graph[46][37]='e';
    graph[85][21]='Q';
    graph[36][4]='c';
    graph[39][2]='t';
    graph[13][76]='m';
    graph[77][96]='i';
    graph[99][19]='o';
    graph[77][85]='6';
    graph[96][19]='r';
    graph[20][13]='N';
    graph[58][79]='v';
    graph[99][16]='Y';
    graph[17][95]='p';
    graph[95][21]='x';
    graph[43][1]='v';
    graph[58][11]='m';
    graph[78][29]='C';
    graph[78][92]='X';
    graph[95][17]='p';
    graph[5][30]='N';
    graph[95][83]='2';
    graph[9][54]='6';
    graph[72][19]='F';
    graph[36][76]='_';
    graph[13][85]='W';
    graph[58][24]='l';
    graph[2][84]='J';
    graph[36][52]='3';
    graph[76][33]='X';
    graph[21][29]='U';
    graph[32][21]='T';
    graph[29][83]='q';
    graph[85][87]='u';
    graph[68][2]='6';
    graph[48][33]='u';
    graph[87][77]='I';
    graph[32][94]='R';
    graph[12][2]='s';
    graph[92][85]='9';
    graph[5][45]='Y';
    graph[13][87]='l';
    graph[83][21]='_';
    graph[73][77]='h';
    graph[58][45]='t';
    graph[68][1]='v';
    graph[36][11]='G';
    graph[52][36]='3';
    graph[99][12]='{';
    graph[52][42]='6';
    graph[32][85]='t';
    graph[30][7]='7';
    graph[31][12]='w';
    graph[100][57]='z';
    graph[57][79]='7';
    graph[96][46]='j';
    graph[77][73]='h';
    graph[33][11]='s';
    graph[96][99]='n';
    graph[37][53]='h';
    graph[46][77]='M';
    graph[87][96]='w';
    graph[68][43]='Z';
    graph[9][37]='I';
    graph[12][84]='W';
    graph[42][73]='c';
    graph[67][2]='A';
    graph[33][79]='2';
    graph[68][84]='1';
    graph[79][22]='z';
    graph[7][30]='7';
    graph[42][24]='z';
    graph[58][22]='Q';
    graph[1][68]='v';
    graph[78][73]='}';
    graph[52][4]='u';
    graph[32][20]='X';
    graph[4][68]='l';
    graph[95][32]='e';
    graph[21][95]='x';
    graph[12][99]='{';
    graph[16][19]='f';
    graph[31][76]='e';
    graph[20][94]='_';
    graph[4][52]='u';
    graph[53][51]='a';
    graph[13][32]='t';
    graph[21][32]='T';
    graph[54][9]='6';
    graph[95][49]='Q';
    graph[36][31]='2';
    graph[9][46]='c';
    graph[49][95]='Q';
    graph[17][83]='s';
    graph[99][96]='n';
    graph[96][87]='w';
    graph[53][63]='u';
    graph[20][33]='D';
    graph[12][96]='k';
    graph[46][19]='t';
    graph[4][84]='q';
    graph[11][76]='j';
    graph[83][29]='q';
    graph[29][21]='U';
    graph[21][85]='Q';
    graph[94][20]='_';
    graph[36][84]='Y';
    graph[73][78]='}';
    graph[24][11]='X';
    graph[9][53]='}';
    graph[53][9]='}';
    graph[48][20]='7';
    graph[2][68]='6';
    graph[83][30]='3';
    graph[48][6]='J';
    graph[32][95]='e';
    graph[37][9]='I';
    graph[31][84]='t';
    graph[4][43]='0';
    graph[6][49]='}';
    graph[5][83]='X';
    graph[24][45]='e';
    graph[53][43]='P';
    graph[79][100]='e';
    graph[84][2]='J';
    graph[87][13]='l';
    graph[13][31]='1';
    graph[84][4]='q';
    graph[45][58]='t';
    graph[73][92]='8';
    graph[42][52]='6';
    graph[20][32]='X';
    graph[100][79]='e';
    graph[52][54]='_';
    graph[12][87]='3';
    graph[29][78]='C';
    graph[85][32]='t';
    graph[37][72]='_';
    graph[73][46]='c';
    graph[92][21]='Q';
    graph[29][5]='0';
    graph[83][5]='X';
    graph[94][95]='Y';
    graph[49][94]='t';
    graph[79][58]='v';
    graph[100][6]='A';
    graph[52][11]='7';
    graph[37][63]='r';
    graph[30][5]='N';
    graph[24][58]='l';
    graph[77][46]='M';
    graph[22][58]='Q';
    graph[4][54]='N';
    graph[79][48]='S';
    graph[83][95]='2';
    graph[29][92]='n';
    graph[31][13]='1';
    graph[85][92]='9';
    graph[94][32]='R';
    graph[54][43]='Y';
    graph[48][100]='o';
    graph[29][45]='{';
    graph[96][12]='k';
    graph[45][22]='T';
    graph[58][33]='W';
    graph[99][2]='F';
    graph[57][7]='8';


    if (getenv("IAMNOOB")){
        int i=0,j=0;
        for (i=0;i<101;i++){
            for (j=0;j<101;j++){
                printf("%c ",graph[i][j]);
            }
            printf("\n");
        }
    }



}

void getinput(){
    char buffer[51];
    int pos[10];

    fgets(buffer,51,stdin);
    char *pch;
    pch = strtok(buffer,",");
    int i=0;
    int ctr=0;
    while (pch != NULL){
        int val=atoi(pch);
        pos[i]=val;
        i+=1;
        ctr+=1;
        pch = strtok (NULL, ",");
    }

    i=0;
    while(i<ctr-1){
        flag[i+idx]=graph[pos[i]][pos[i+1]];
        i+=1;
        }
    idx+=(ctr-1);

}
void printinstructions(){
printf("                _____            ____          _           \n");
printf("               |_   _|__  _ __  / ___|___   __| | ___ _ __ \n");
printf("                 | |/ _ \\| '_ \\| |   / _ \\ / _` |/ _ \\ '__|\n");
printf("                 | | (_) | |_) | |__| (_) | (_| |  __/ |   \n");
printf("                 |_|\\___/| .__/ \\____\\___/ \\__,_|\\___|_|   \n");
printf("                         |_|                               \n");
printf("I like competitive coding and I also like reversing, so here is my reversing challenge for you\nCue Story \n\n");
printf("You are a traveller in ancient lands\n");
printf("You suddenly encounter an old tree. He knows what you seek\n");
printf("He gives you a map, hundered and one cross hundred and one \n");
printf("Now the tree says:\n\n");
printf("\t\"I once fought a bad wizard and he turned me into a tree, He tore the spell and threw it away in this maze.\"\n");
printf("\t\"Find me the spell o dear traveller and I will give you what you seek\"");

printf("\t\"Every path which is safe contains a piece of what you seek\"\n");
printf("\t\"Every path which is unsafe contains squigly line(~) representing a crack. It would be unsafe to go there, but you are your own master\"\n");
printf("\t\"I still know some magic, so I will put you in the starting room and you would need to reach the last room, picking up the pieces along the way\"\n");
printf("\t\"Use the map and decide the next room you want to go to\"\n");
printf("\t\"I am dying so please do it quickly\"\n\n");

printf("Saying this he falls asleep and you are left alone.\n");
printf("Your job, should you choose to accept it, is to find the torn pieces and return them to the tree\n");
printf("You have 7 testcases\n");
printf("For each testcase, you will get the starting room and the ending room\n");
printf("As the input provide me a comma separated line of the rooms you wish to go to including the starting and ending room.\n");

printf("For example, 99,96,12,96,77 will give you nkki\n");
printf("Are you ready??\n");

}

int main(){
    printinstructions();
    initialize();
    printf("\n[+]Go from 100 to 72: ");
    getinput();
    printf("\n[+]Go from 6 to 63: ");
    getinput();
    printf("\n[+]Go from 49 to 51: ");
    getinput();
    printf("\n[+]Go from 17 to 1: ");
    getinput();
    printf("\n[+]Go from 30 to 39: ");
    getinput();
    printf("\n[+]Go from 7 to 67: ");
    getinput();
    printf("\n[+]Go from 57 to 16: ");
    getinput();

    printf("\n\n\"O my dear traveller, you are back. Here is what you seek. If its not what you want maybe it's your fault\"\n\n\t%s\n",flag);
}
