# Compile All
# compA.py -> compileall.rs
import shutil
from pathlib import Path
import getC
import buildSys
import getH
import time
import os
import regex
def comp(bdir,fdir,files,clean,rmvf,mode,fin,binmode,fout):
    if(os.path.exists(fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))):
        os.remove(fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))
    shutil.copytree(fdir,bdir+"\\"+Path(Path(fin).name).stem,ignore=shutil.ignore_patterns("__ROSIE_BIN__"))
    definelist = []
    repllist = []
    for i in files:
        included = regex.findall(r"(?:(?<=\/)[^\/]*)$",i)
        nwincluded = (None if included.__len__()<1 else "_"+included[0].capitalize()+"_")
        nwrepl = (None if included.__len__()<1 else included[0])
        definelist.append(nwincluded) if nwincluded!=None else None
        repllist.append(nwrepl) if nwrepl!=None else None
    for i in files:
        fpath = regex.sub(r"\.rose(\.rose)*",".rose",Path(bdir+"\\"+Path(Path(fin).name).stem+"\\"+i+".rose").resolve().__str__())
        opath = regex.sub(r"\.rose","",Path(bdir+"\\"+Path(Path(fin).name).stem+"\\"+i+".rose").resolve().__str__())
        cdata = getH.gH(fpath)
        cfile = getC.cF(cdata[2],cdata[0],Path(i).stem,repllist,definelist,cdata[3])
        hxxnamespaces = []
        for i in cdata[3]:
            readf = open(Path(fpath).parent.__str__()+"\\"+Path(i).__str__()+".hxx","r")
            try:
                hxxnamespaces.append(regex.sub("\"","",regex.search(r"#define NAMESPACE (.*);",readf.read()).group(1)))
            except:
                readf.close()
                print("Error no namespace defined in file: "+Path(fpath).parent.__str__()+"\\"+Path(i).__str__()+".hxx")
                exit(1)
            readf.close()
        for i in hxxnamespaces:
            cfile[0] = regex.sub(i+r"\.([^\w]*)",i+r"::\1",cfile[0])
        os.rename(fpath,opath+(".cxx" if cfile[1] else ".hxx"))
        wfile = open(opath+(".cxx" if cfile[1] else ".hxx"),"w")
        wfile.write(cfile[0])
        wfile.close()
    if(binmode):
        if mode=="scons":
            buildSys.scons(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__(),Path(fin).name)
            shutil.copy2(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__()+"\\"+regex.sub(".rose","",Path(fin).name+".exe"),fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))
        if mode=="gcc":
            buildSys.gcc(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__(),Path(fin).name)
            shutil.copy2(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__()+"\\"+regex.sub(".rose","",Path(fin).name+".exe"),fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))            
        if mode=="clang":
            buildSys.clang(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__(),Path(fin).name)
            shutil.copy2(Path(bdir+"\\"+Path(fdir).stem.__str__()).resolve().__str__()+"\\"+regex.sub(".rose","",Path(fin).name+".exe"),fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))
        if mode=="make":
            buildSys.cmake(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__(),Path(fin).name)
            shutil.copy2(Path(bdir+"\\"+Path(Path(fin).name).stem).resolve().__str__()+"\\Debug\\"+regex.sub(".rose","",Path(fin).name+".exe"),fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))
    else:
        if(os.path.exists(fout+"\\"+Path(fdir).name)):
            shutil.rmtree(fout+"\\"+Path(fdir).name)
        shutil.copytree(bdir+"\\"+Path(fdir).name,fout+".exe")
    if(clean):
        while(os.path.exists(fout+"\\"+regex.sub(".rose","",Path(fin).name+".exe"))==False):
            time.sleep(0.2)
        if(os.path.exists(bdir)):
            shutil.rmtree(Path(bdir).parent.__str__())
        for i in rmvf:
            try:
                shutil.rmtree(fdir+"\\"+Path(fdir+"\\"+Path(i).__str__().split()[0]).stem)
            except FileNotFoundError:
                pass
