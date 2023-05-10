import sys
import os
import getH
import getC
from pathlib import Path
cont = False
try:
    fin = sys.argv[1]
    cont = True
except:
    print("Input file missing")
mpath = "C:/Program Files/Mool/"
try:
    fout = sys.argv[1]
except:
    fout = os.getcwd()
if(cont):
    cdata = getH.gH(fin)
    cfile = getC.cF(cdata[2],cdata[0],Path(fin).stem)
    print(cfile)