#include <string>
#define NAMESPACE "_CONV";
#ifndef _CONV
#define _CONV
std::string mk_str_int(int obj){
    return std::to_string(obj);
}
std::string mk_str_bool(bool obj){
    return (obj)?"true":"false";
}
int mk_int_bool(bool obj){
    return (obj)?1:0;
}
int mk_int_str(std::string obj){
    return std::stoi(obj);
}
bool mk_bool_str(std::string obj){
    return (obj=="true");
}
bool mk_bool_int(int obj){
    return (obj==1);
}
#endif
