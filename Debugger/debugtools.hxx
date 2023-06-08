#include <fstream>
#include <string>
#ifndef __DEBUGTOOLS__
#define __DEBUGTOOLS__
bool passbrackets(int *line, std::string fileread){
    int openbrackets[3] = {0,0,0};
    int startbracket[3] = {0,0,0};
    int currentline = 1;
    for(int i=0;i<fileread.length();i++){
        if(fileread[i] == '{'){if(openbrackets[0] == 0){startbracket[0] = currentline;};openbrackets[0] += 1;}
        if(fileread[i] == '}'){openbrackets[0] -= 1;}       
        if(fileread[i] == '['){if(openbrackets[1] == 0){startbracket[1] = currentline;}openbrackets[1] += 1;}
        if(fileread[i] == ']'){openbrackets[1] -= 1;}                 
        if(fileread[i] == '('){if(openbrackets[2] == 0){startbracket[2] = currentline;}openbrackets[2] += 1;}
        if(fileread[i] == ')'){openbrackets[2] -= 1;}
        if(fileread[i] == '\n'){currentline += 1;}
    }
    if(openbrackets[0] == 0){
        if(openbrackets[1] == 0){
                if(openbrackets[2] == 0){
                    return true;
                }else{
                    *line = startbracket[2];
                    return false;
                }
        }else{
            *line = startbracket[1];
            return false;
        }
    }else{
        *line = startbracket[0];
        return false;
    }
}
bool passstring(int *line, std::string fileread){
    int stringcount[2] = {0,0};
    int startstring[2] = {0,0};
    int currentline = 1;
    for(int i=0;i<fileread.length();i++){
        if(fileread[i]=='\"'){stringcount[0]++;startstring[0]=currentline;}
        if(fileread[i]=='\''){stringcount[1]++;startstring[1]=currentline;}       
        if(fileread[i]=='\n'){currentline++;}
    }
    if((stringcount[0]%2)!=0){
        *line = startstring[0];return false;
    }else{
        if((stringcount[1]%2)!=0){
            *line = startstring[1];return false;
        }else{
            return true;
        }
    }
}
std::string debug(std::string filename){
    std::string fileline;
    std::string filedata;
    std::ifstream fstring(filename);
    while(std::getline (fstring,fileline)){filedata = filedata + fileline + "\n";}
    fstring.close();
    int errortrace;
    if(!passbrackets(&errortrace,filedata)){return "Unclosed brackets on line: [" + std::to_string(errortrace) + "] in file: " + filename;}
    if(!passstring(&errortrace,filedata)){return "Unclosed string on line: [" + std::to_string(errortrace) + "] in file: " + filename;}
    return "pass";
}
#endif