# Rosie command
# Rosie.py -> rosie.rs
import sys
import regex
import Cmkdir
import Htree
import subprocess
import random
import compA
import os
import HandleOS
import time
import readagrv
from pathlib import Path
HandleOS.initcommand()
cont = False
args = readagrv.read(sys.argv)
isdebugged = args[5]
setbuild = args[4]
binmode = args[3]

clean = args[2]

fout = args[1]
fin = args[0]
mpath = HandleOS.getinstall()+"\\rosie"
if(setbuild != "check"):
    os.environ["compiler"] = setbuild
else:
    HandleOS.initcommand()
    setbuild = os.environ["compiler"]
if(os.path.exists(fin)==False):
    print("error: file dose not exist")
    exit(1)

if(fin != ""):
    cont = True
if(cont):
    tmpdir = fout+"/__ROSIE_BIN__/"+Path(fin).stem+random.random().hex()
    Cmkdir.mkdir(fout+"/__ROSIE_BIN__/")
    Cmkdir.mkdir(tmpdir)
    builds = Htree.Htree(Path(fin).parent.__str__(),fin,mpath)
    if(isdebugged):
        strlist = fin+".rose+"
        for i in builds[0]:
            strlist = strlist + Path(tmpdir + "\\" + i).absolute().__str__() + ".rose"
        strlist = regex.sub("\.rose(\.rose)*",".rose+",strlist)
        strlist = regex.sub("\+\+*","+",strlist)
        debug = subprocess.Popen(mpath+"\\bin\\debugger.exe \""+strlist+"\"")
        while(debug.poll()==None):
            time.sleep(0.2)
        if(debug.returncode):
            exit(1)
    builds[0].append(Path(fin).name)
    compA.comp(tmpdir,Path(fin).parent.__str__(),builds[0],clean,builds[1],setbuild,fin,binmode,fout)
sys.exit(0)
#    cdata = getH.gH(fin)
#    cfile = getC.cF(cdata[2],cdata[0],Path(fin).stem)
    