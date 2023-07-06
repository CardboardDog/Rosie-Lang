#define NAMESPACE "_REGEX";
#include <iostream>
#include <string>
#include <regex>
#ifndef _REGEX
#define _REGEX
std::string _sub(std::string _in, std::string _pattern, std::string _rep){
    std::regex ex(_pattern);
    return std::regex_replace(_in,ex,_rep);
}
std::vector<std::string> _search(std::string _in, std::string _pattern){
    std::regex ex(_pattern);
    std::smatch matches;
    std::regex_search(_in,matches,ex);
    std::vector<std::string> rtrn;
    for(int i=0;i<matches.length();i++){
        rtrn.push_back(matches[i]);
    }
    return rtrn;
}
#endif