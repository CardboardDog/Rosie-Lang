import regex as re
def cF(fl, hdrs, name):
    # get file mode
    ishdr = (re.search("mode header",fl) == None)
    # replace "add [file]" with an empty comment"
    nwfl = re.sub("add.*","// include",fl)
    # remove returns that come after "{" 
    nwfl = re.sub("{\n","{",nwfl)
    # add semi-colons to the end of each line
    nwfl = re.sub("\n",";",nwfl)
    # replace str with String
    nwfl = re.sub("str ","std::string ", nwfl)
    # remove indents
    nwfl = re.sub("\s+"," ",nwfl)
    # remove the empty comments
    nwfl = re.sub("// include;","",nwfl)
    # fix semi-colons bug
    nwfl = re.sub(";;",";",nwfl)
    # convert functions to autos
    nwfl = re.sub("fn","auto",nwfl)
    nwfl = re.sub("(?<=auto .*)\("," = [](",nwfl)

    # add header/script specific things
    if(ishdr):
        # add main function
        nwfl = "int main(){"+nwfl+"return 1;}"
    else:
        # add c++ directives and remove cool directives
        nwfl = "ifdef "+name+"\ndefine "+name+"\n"+nwfl+"\nendif"
        nwfl = re.sub("mode header;","",nwfl)
    return nwfl