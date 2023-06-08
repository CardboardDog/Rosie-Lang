#define NAMESPACE "_FSYS";
#include <fstream>
#include <string>
#ifndef _FSYS
#define _FSYS
class _reader{
    public:
        std::ifstream _freader;
        _reader(std::string location){
            this->_freader = std::ifstream(location);
        }
        void close(){
            this->_freader.close();
        }
        std::string read(){
            std::string returnstr;
            std::string line;
            while(std::getline(this->_freader,line)){returnstr=returnstr+line+"\n";}
            return returnstr;
        }
};
class _writer{
    public:
        std::ofstream _fwriter;
        _writer(std::string location){
            this->_fwriter = std::ofstream(location);
        }
        void close(){
            this->_fwriter.close();
        }
        std::string write(std::string input){
            this->_fwriter << input;
        }
};
#endif