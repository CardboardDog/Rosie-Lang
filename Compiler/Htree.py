# HEADER TREE
# Htree.py -> headertree.rs
import getH
import shutil
from pathlib import Path
def Htree(pth,fl,libpth):
    nwfl = fl
    hdrs = getH.gH(nwfl)[0]
    tmphdrs = hdrs
    rtrn = True
    allhdrs = hdrs
    rmvltr = []
    while(rtrn):
        nwhdrs=[]
        for i in tmphdrs:
            if(Path(libpth+"/pckg/"+i+".rose").exists()):
                rmvltr.append(Path(i).parent.name)
                try:
                    shutil.copytree(Path(libpth+"/pckg/"+i+".rose").parent.__str__(),pth+"\\"+Path(libpth+"/pckg/"+i+".rose").parent.stem)
                except FileExistsError:
                    pass
                except:
                    print("Error: cannot write to: "+pth+"\\"+Path(libpth+"/pckg/"+i+".rose").parent.stem)
            if(Path(pth+"\\"+i+".rose").exists()):
                for ii in getH.gH(pth+"\\"+i+".rose")[0]:
                    nwhdrs.append(ii)
            else:
                pass
        tmphdrs = nwhdrs
        if(nwhdrs == []):
            rtrn = False
        else:
            for i in nwhdrs:
                allhdrs.append(i)
    return allhdrs,rmvltr
