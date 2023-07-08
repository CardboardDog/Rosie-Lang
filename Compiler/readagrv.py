from pathlib import Path
def read(args):
    makemode = "check"
    if "-i" in args:
        indir = args[args.index("-i")+1]
    else:
        indir = args[1]
    if(("--cmake" in args)):
        makemode = "make"
    if(("--gcc" in args)):
        makemode = "gcc"
    if(("--scons" in args)):
        makemode = "scons"
    if(("--clang" in args)):
        makemode = "clang"
    if(("-o" in args)):
        outdir = args[args.index("-o")+1]
    else:
        outdir=Path(indir).parent.__str__()
    return (indir,outdir,(("--clean=false" in args)==False),("--exe=false" in args) == False,makemode,(("--debug=false" in args)==False),(("-q" in args)==True))
