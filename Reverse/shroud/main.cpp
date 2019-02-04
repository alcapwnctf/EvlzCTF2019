#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <sstream>
#include <iterator>
#include <map>

using namespace std;

void run (string command){
    system(command.c_str());
}

int checkParity(string waduString){
    int paritybit;
    paritybit=isupper(waduString[0])?1:0;
    int val=0;
    for(unsigned int i=1;i<waduString.length();i++){
        if (isupper(waduString[i]))val^=1;
        else val^=0;
    }
    return val==paritybit;
}

char strToChar(string str, int key) {
    int parsed = 0;
    for (int i=1; i<8; i++) {
        if (str[i]=='1') {
            parsed |= 1<<(7-i);
        }
    }
    parsed=parsed^key;
    return (char)parsed;
}

string interpret(vector <string> commList){
    string command="";
    map<string, int> waduhekkmap;

    waduhekkmap.insert(pair<string, int>("WADUHEKK", 79));
    waduhekkmap.insert(pair<string, int>("WAduHekK", 120));
    waduhekkmap.insert(pair<string, int>("WadUhEkK", 39));
    waduhekkmap.insert(pair<string, int>("waDUHEkk", 15));
    waduhekkmap.insert(pair<string, int>("wADuHeKk", 94));
    waduhekkmap.insert(pair<string, int>("wadUhEKK", 34));
    waduhekkmap.insert(pair<string, int>("wAdUHEkk", 106));
    waduhekkmap.insert(pair<string, int>("WaDUHekk", 15));
    waduhekkmap.insert(pair<string, int>("waduHEKK", 55));
    waduhekkmap.insert(pair<string, int>("wADUHeKK", 66));
    waduhekkmap.insert(pair<string, int>("wAdUhEkK", 52));
    waduhekkmap.insert(pair<string, int>("wadUHeKK", 121));
    waduhekkmap.insert(pair<string, int>("WaduhEKK", 100));
    waduhekkmap.insert(pair<string, int>("WaduHEkK", 105));
    waduhekkmap.insert(pair<string, int>("WADuhEkk", 1));
    waduhekkmap.insert(pair<string, int>("WaDuhEKk", 64));
    waduhekkmap.insert(pair<string, int>("WaduhekK", 102));
    waduhekkmap.insert(pair<string, int>("wADuheKK", 11));
    waduhekkmap.insert(pair<string, int>("waDUheKK", 90));
    waduhekkmap.insert(pair<string, int>("WAduHeKk", 32));
    waduhekkmap.insert(pair<string, int>("wADuhekk", 11));
    waduhekkmap.insert(pair<string, int>("waduHeKk", 102));
    waduhekkmap.insert(pair<string, int>("wADUhEkk", 25));
    waduhekkmap.insert(pair<string, int>("WaduHekk", 102));
    waduhekkmap.insert(pair<string, int>("waDuHEkK", 66));
    waduhekkmap.insert(pair<string, int>("WADUhEkK", 5));
    waduhekkmap.insert(pair<string, int>("wAdUHekK", 40));
    waduhekkmap.insert(pair<string, int>("waDuheKk", 80));
    waduhekkmap.insert(pair<string, int>("WADuHeKK", 24));
    waduhekkmap.insert(pair<string, int>("WADuhEKK", 19));
    waduhekkmap.insert(pair<string, int>("WaDUHEkK", 72));
    waduhekkmap.insert(pair<string, int>("waduhekk", 118));
    waduhekkmap.insert(pair<string, int>("wAdUheKK", 36));
    waduhekkmap.insert(pair<string, int>("wADuhEKk", 30));
    waduhekkmap.insert(pair<string, int>("waDUHekK", 64));
    waduhekkmap.insert(pair<string, int>("WaDUhekK", 75));
    waduhekkmap.insert(pair<string, int>("WadUHekK", 88));
    waduhekkmap.insert(pair<string, int>("waDuhekK", 99));
    waduhekkmap.insert(pair<string, int>("waduhEkK", 70));
    waduhekkmap.insert(pair<string, int>("wADuHEKK", 43));
    waduhekkmap.insert(pair<string, int>("wadUhEkk", 81));
    waduhekkmap.insert(pair<string, int>("waduHEkk", 74));
    waduhekkmap.insert(pair<string, int>("WAduhEKk", 1));
    waduhekkmap.insert(pair<string, int>("wadUhekK", 89));
    waduhekkmap.insert(pair<string, int>("WaDUhEKK", 126));
    waduhekkmap.insert(pair<string, int>("wADUHEKk", 52));
    waduhekkmap.insert(pair<string, int>("WAdUhEkk", 31));
    waduhekkmap.insert(pair<string, int>("wADUhekK", 61));
    waduhekkmap.insert(pair<string, int>("WaDuHekK", 100));
    waduhekkmap.insert(pair<string, int>("wAduheKk", 12));
    waduhekkmap.insert(pair<string, int>("WAdUhekK", 30));
    waduhekkmap.insert(pair<string, int>("WaduhEkk", 84));
    waduhekkmap.insert(pair<string, int>("waDuHekk", 121));
    waduhekkmap.insert(pair<string, int>("WadUheKK", 65));
    waduhekkmap.insert(pair<string, int>("WADUHekK", 42));
    waduhekkmap.insert(pair<string, int>("waDUhekk", 100));
    waduhekkmap.insert(pair<string, int>("WADUHeKk", 47));
    waduhekkmap.insert(pair<string, int>("wadUHEKk", 72));
    waduhekkmap.insert(pair<string, int>("WAdUhEKK", 0));
    waduhekkmap.insert(pair<string, int>("wADUhEKK", 47));
    waduhekkmap.insert(pair<string, int>("wADuHekK", 48));
    waduhekkmap.insert(pair<string, int>("wadUHekk", 66));
    waduhekkmap.insert(pair<string, int>("WAduheKK", 98));
    waduhekkmap.insert(pair<string, int>("WAduHEkk", 110));
    waduhekkmap.insert(pair<string, int>("WadUHeKk", 57));
    waduhekkmap.insert(pair<string, int>("WaduHeKK", 47));
    waduhekkmap.insert(pair<string, int>("WAdUheKk", 119));
    waduhekkmap.insert(pair<string, int>("WadUhekk", 54));
    waduhekkmap.insert(pair<string, int>("WaDuHEkk", 11));
    waduhekkmap.insert(pair<string, int>("WADuheKk", 74));
    waduhekkmap.insert(pair<string, int>("waDuHEKk", 7));
    waduhekkmap.insert(pair<string, int>("wADUHekk", 82));
    waduhekkmap.insert(pair<string, int>("waduHekK", 34));
    waduhekkmap.insert(pair<string, int>("WAduhEkK", 105));
    waduhekkmap.insert(pair<string, int>("WAdUHeKK", 118));
    waduhekkmap.insert(pair<string, int>("WaDUHEKk", 16));
    waduhekkmap.insert(pair<string, int>("WADuHEKk", 65));
    waduhekkmap.insert(pair<string, int>("waDUhEkK", 15));
    waduhekkmap.insert(pair<string, int>("WAdUHekk", 99));
    waduhekkmap.insert(pair<string, int>("WADuHEkK", 81));
    waduhekkmap.insert(pair<string, int>("WaduHEKk", 51));
    waduhekkmap.insert(pair<string, int>("wAduHeKK", 117));
    waduhekkmap.insert(pair<string, int>("waDUHeKk", 5));
    waduhekkmap.insert(pair<string, int>("WAduhekk", 0));
    waduhekkmap.insert(pair<string, int>("waDuHeKK", 112));
    waduhekkmap.insert(pair<string, int>("WaDUHeKK", 103));
    waduhekkmap.insert(pair<string, int>("WadUHEkk", 65));
    waduhekkmap.insert(pair<string, int>("WaDuHeKk", 116));
    waduhekkmap.insert(pair<string, int>("wAdUHEKK", 0));
    waduhekkmap.insert(pair<string, int>("WaDuhekk", 64));
    waduhekkmap.insert(pair<string, int>("WaduheKk", 121));
    waduhekkmap.insert(pair<string, int>("WaDUheKk", 78));
    waduhekkmap.insert(pair<string, int>("waDUHEKK", 66));
    waduhekkmap.insert(pair<string, int>("waDUhEKk", 72));
    waduhekkmap.insert(pair<string, int>("WadUHEKK", 63));

    for(unsigned int i=0;i<commList.size();i++){
        string binStr="0";
        for(int j=1;j<8;j++){
            if (isupper(commList[i][j]))binStr+='1';
            else binStr+='0';
        }
        string val=commList[i];
        command+=strToChar(binStr,waduhekkmap[commList[i]]);
        if(const char* env_p = getenv("IAMNOOB"))cout<<command<<endl;
    }

    return command;
}

string convert(vector <string> commList){
    bool correct=true;
    for(unsigned int i=0;i<commList.size();i++){
        if(!checkParity(commList[i])){
            correct=false;
            break;
        }
    }
    if(correct)return interpret(commList);
    else return "exit";
}

vector <string> split(char *command){
    char *nextCommand;
    vector <string> commandList;

    nextCommand=strtok(command," ");

    while(nextCommand!=NULL){
        commandList.push_back(nextCommand);
        nextCommand=strtok(NULL," ");
    }
    return commandList;
}

int main(int argc, char const *argv[])
{
    char buffer[1025];
    char intro1[]="WADuhEkk WaduhEKK wADuheKK waDuHEkK WadUHEKK wadUhekK WADuhEkk waduHeKk waduHeKk waDuHEkK WadUHEKK wAdUhEkK WaduHekk WaduHEkK WadUHEKK wAdUheKK WADuhEkk waduHeKk WaduhEKK waDuHEkK wADUhEkk WADuhEkk WadUHEKK WADuhEKK waDuHEkK WadUHEKK WAdUhEKK wAdUhEkK WaduHEkK WaDUHEkK waduhEkK wAdUhEkK WADuHeKK WADuhEKK WaDUHEKk WadUHEKK wAduheKk waDuHEkK WADuhEKK WADuhEkk WadUHEKK WADuhEKK wADuheKK wAdUhEkK WADuhEKK WadUHEKK WaDUhEKK WadUHEKK waDuHEkK WaduHekk waduHeKk waDUHekK WadUHEKK WaDUHEkK WaduHekk WaduHEkK WADuhEkk waDuheKk WADuHeKK WADuhEKK wAdUhEkK WaduHekk WaduHEkK WadUHEKK wAdUheKK wAdUhEkK WaduHEkK WaDUHEkK wADuheKK WADuhEkk wADuhekk wADuhekk";
    char intro2[]="WADuhEkk WaduhEKK wADuheKK waDuHEkK WadUHEKK waDUhekk WADuhEkk waduHeKk waduHeKk WadUHEKK wADUhEkk WADuhEkk WadUHEKK wAdUheKK wADuheKK wAdUhEkK WADuhEKK WadUHEKK WADuhEKK waDuHEkK WadUHEKK WaduHEkK waDuHEkK waDUHeKk waDUHeKk";
    run(convert(split(intro1)));
    run(convert(split(intro2)));
    cout<<">>";
    cin.getline(buffer,1025,'\n');
    run(convert(split(buffer)));
    return 0;
}
