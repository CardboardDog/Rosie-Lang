#include <vector>
#ifndef __INPUTREADER__
#define __INPUTREADER__
void readinput(char *fs[], std::vector<std::string>*outputvect){
    outputvect->clear();
    std::string stringfs(fs[1]);
    std::string tempstring;
    for(int i=0;i<stringfs.length();i++){
        if(fs[1][i] == '+'){
            outputvect->push_back(tempstring);
            tempstring.clear();
        }else{
            tempstring = tempstring + fs[1][i];
        }
    }
}
#endif