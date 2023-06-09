import urllib.request
import os
import zipfile
import sys
import json
import subprocess
import shutil
from pathlib import Path
def make_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass
    except PermissionError:
        print("Error: please run as administrator, you do not have permission to install Rosie")
        exit(1)
def move(name, location):
    try:
        os.rename(name,location+"\\"+Path(name).name)
    except:
        pass
last_release ="https://github.com/CardboardDog/Rosie-Lang/releases/download/manual-windows/Rosie1.0.zip"
extract = os.getcwd()+"/rosie-temp.zip"
temp = os.getcwd()+"/rosie-temp"
print("installing rosie")
print("- retrieving rosie Win R1.0")
urllib.request.urlretrieve(last_release,extract)
print("- extracting")
if(zipfile.is_zipfile(extract)):
    print("- reading install.json")
    zipfile.ZipFile(extract).extractall(temp)
    install_info = json.loads(open(temp+"/install.json").read())
    install = install_info["extract"] + install_info["install"]
    print("- installing at "+install)
    print("- creating directories")
    make_dir(install)
    for i in install_info["require"]:
        make_dir(install+i)
    for i in install_info["relocate"]:
        print("- installing "+i)
        move(temp+"\\"+i,install+"\\"+install_info["relocate"].get(i))
    print("- adding rosie/bin to path")
    subprocess.Popen("powershell -command "+"\""+"[Environment]::SetEnvironmentVariable('Path', $env:Path + ';C:\\Program Files\\rosie\\bin', 'Machine')"+"\"")
    print("- removing rosie-temp")
    shutil.rmtree(temp)
    print("- removing rosie-temp.zip")
    os.remove(extract)
    print("install complete, please close all restart powershell to use rosie")

else:
    print("- error: cannot download rosie, please check your internet")
    sys.exit(1)

