#include <string>
#define NAMESPACE "_OS";
#ifndef _OS
#define _OS
int _terminal(std::string cmd){
    return std::system(cmd.c_str());
}
std::string _osname(){
    #ifdef _WIN64
    return "Windows";
    #elif _WIN32
    return "Windows";
    #elif __APPLE__ || __MACH__
    return "Mac OSX";
    #elif  __linux__
    return "Linux";
    #elif __unix || __unix__
    return "Unix";
    #elif __FreeBSD__
    return "FreeBSD";
    #else
    return "Unknown";
    #endif
}
#endif
