#include <iostream>
#include "debugtools.hxx"
#include "inputreader.hxx"
int main(int argc,char *argv[]){
    std::vector<std::string> inputfiles;
    bool passed = true;
    readinput(argv,&inputfiles);
    for(int i=0;i<(inputfiles.size());i++){
        std::string fileres = debug(inputfiles[i]);
        if(fileres!="pass"){std::cout << fileres << std::endl;passed=false;}
    }
    return int(passed!=true);
}