import subprocess
import time
import os
import shlex
import HandleOS
def run(commands):
    command = ""
    for i in commands:
        if(HandleOS.getos()=="windows"):
            command = command+i+"& "
        else:
            command = command+i+"; "
    """if HandleOS.getos()=="windows":
        command = "powershell.exe&"+command+""
    """
    cmd = subprocess.Popen(command[:-2], shell=True)
    cmd.wait()