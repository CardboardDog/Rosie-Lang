def gH(fin):
    inc = []
    fdata = open(fin, "r").read().split("\n")
    for i in fdata:
        sdata = i.split(" ")
        if(sdata[0] == "add"):
            inc.append(sdata[1])
    return (inc, sdata, open(fin, "r").read())