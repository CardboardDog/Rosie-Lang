# Handle Operating System
# HandleOS.py -> handleos.rs
import platform
import subprocess
import os
def getinstall():
    if(getos()=="linux"):
        return "/usr/bin/"
    if(getos()=="windows"):
        return "C:/Program Files/"
def initcommand():
    """
    [Warning! support for CMake and SCons has ended do to CLI issues]

    if(subprocess.getstatusoutput("scons -h")[0] == 0):
        os.environ["compiler"] = "scons"
        return

    if(subprocess.getstatusoutput("cmake --help")[0] == 0):
        os.environ["compiler"] = "make"
        return
    """
    if(subprocess.getstatusoutput("g++ --help")[0] == 0):
        os.environ["compiler"] = "gcc"
        return
    """if(subprocess.getstatusoutput("clang")[0] == 0):
        os.environ["compiler"] = "clang"
        return
    """
def getcompiler(fname,bdir):
    if(os.environ["compiler"]=="make"):
        command = [
            "cd "+bdir,
            "cmake"
        ]
    if(os.environ["compiler"]=="scons"):
        command = [
            "cd "+bdir,
            "scons"
        ]
    if(os.environ["compiler"]=="gcc"):
        command = [
            "cd "+bdir,
            "g++ "+fname+".cxx -o "+bdir+"\\build\\"+fname+".exe"
        ]
    if(os.environ["compiler"]=="clang"):
        command = [
            "cd "+bdir,
            "clang++ -Wall -std=c++11 "+fname+".cxx -o "+fname+".exe"
        ]
    return (os.environ["compiler"],command)
def getos():
    if(platform.system().lower() == "darwin"):
        return "mac"
    else:
        return platform.system().lower()