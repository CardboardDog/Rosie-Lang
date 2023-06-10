import regex
import HandleOS
import subprocess
import time
import cli
import os
def cmake(dir,name):
    cwd = os.getcwd()
    mkfile = open(dir+"\\CMakeLists.txt","w")
    mkfile.write("cmake_minimum_required (VERSION 3.10)\nproject("+regex.sub(".rose","",name)+")\nadd_executable(\""+regex.sub(".rose","",name)+"\" \""+regex.sub(r"\.cxx(\.cxx)*",".cxx",regex.sub(".rose",".cxx",name))+"\")")
    os.chdir(dir)
    cli.run(["cd \""+dir+"\"","cmake \""+dir+"\"","echo ******************","cmake --build \""+dir+"\"","echo --"])
    os.chdir(cwd)
def scons(dir,name):
    mkfile = open(dir+"\\SConstruct","w")
    mkfile.write("Program(\""+regex.sub(".rose","",name)+"\",\""+regex.sub(r"\.cxx(\.cxx)*",".cxx",regex.sub(".rose",".cxx",name)+".exe")+"\")")
    cli.run(["cd \""+dir+"\"","dir","scons -Q"])
def gcc(dir,name):
    cli.run(["cd \""+dir+"\"","c++ "+regex.sub(r"\.cxx(\.cxx)*",".cxx",regex.sub(".rose",".cxx",name))+" -o "+regex.sub(".rose","",name)+".exe"+" -w"])
def clang(dir,name):
    cli.run(["cd \""+dir+"\"","clang++ -Wall -std=c++11 "+regex.sub(r"\.cxx(\.cxx)*",".cxx",regex.sub(".rose",".cxx",name))+" -o "+regex.sub(".rose","",name)+".exe"])