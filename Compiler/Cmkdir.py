# Clean mkdir
# Cmkdir.py -> cleanmkdir.rs
import os
def mkdir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass
    except:
        print("Failed to create "+dir+"")
def mkfl(loc,text):
    try:
        open(loc,"w").write(text)
    except:
        pass
