#define NAMESPACE "_IO";
#include <iostream>
#include <string.h>
#ifndef _IO
#define _IO
void _out(std::string x){
    std::cout << x;
}
std::string _in(){
    std::string inp;
    std::cin >> inp;
    return inp;
}
#endif
