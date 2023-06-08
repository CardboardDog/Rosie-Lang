# GET HEADERS
# getH.py -> getheaders.rs
def gH(fin):
    inc = []
    hinc = []
    fdata = open(fin, "r").read().split("\n")
    for i in fdata:
        sdata = i.split(" ")
        if(sdata[0] == "add"):
            if(sdata[1] != "hxx"):
                inc.append(sdata[1])
            else:
                hinc.append(sdata[2])
    return [inc, sdata, open(fin, "r").read(),hinc]