# Get C++
# getC.py -> convert.rs
import regex as re
def cF(fl, hdrs, name, repl, define, hxx):
    # replace "list" with vector
    nwfl = re.sub(r"([^A-z]*)((([^A-z])list ) *([^ ]*))",r"\1\4std::vector<\5>",fl)
    # add return to end of file
    nwfl = nwfl + "\n"
    # replace namespace.object with _Namespace_::object;
    loop = 0
    for i in repl:
        nwfl = re.sub(i+r"\.([^\w]*)",define[loop]+r"::\1",nwfl)
        loop+=1;
    # replace [] brackets with {}
    nwfl = re.sub(r"(\[)(.*,.*)(\])",r"{\2}",nwfl)
    # add public to classes
    nwfl = re.sub(r"class *([^\{]*)\{([^\}]*)",r"class \1{public:\2",nwfl)
    # replace for(int in int) with c++ for statement
    nwfl = re.sub(r"for(?: *)\(([^ ]*) *in *([^)]*)",r"for(int \1=0;\1<\2;\1++",nwfl)
    # get file mode
    ishdr = (re.search("mode header",nwfl) == None)
    # convert comments
    nwfl = re.sub(r"@{2}[^\}]*@{2}",r"",nwfl)
    nwfl = re.sub(r"@[^\n]*",r"",nwfl)
    # replace "add [file]" with an empty comment"
    nwfl = re.sub(r"add.*",r"// include",nwfl)
    # remove returns that come after "{" 
    nwfl = re.sub(r"{\n",r"{",nwfl)
    # add semi-colons to the end of each line
    nwfl = re.sub(r"\n",r";",nwfl)
    # replace str with String
    nwfl = re.sub(r"([^A-z])str([^A-z])",r"\1std::string\2", nwfl)
    # replace var with auto
    nwfl = re.sub(r"var ",r"auto ", nwfl)
    # remove indents
    nwfl = re.sub(r"\s+",r" ",nwfl)
    # remove the empty comments
    nwfl = re.sub(r"// include;",r"",nwfl)
    # fix semi-colons bug
    nwfl = re.sub(r";+",r";",nwfl)
    # fix :; bug
    nwfl = re.sub(r"public:;","public:",nwfl)
    # convert functions to autos/lambda
    if(not ishdr):
        nwfl = re.sub(r"fn",r"auto",nwfl)
    else:
        nwfl = re.sub(r"fn",r"auto",nwfl)
        nwfl = re.sub(r"(?<=auto [^\(]+)\(",r" = [](",nwfl)
    # add header/script specific things
    if(ishdr):
        # add main function
        nwfl = "int main(){"+nwfl+"return 0;}"
    else:
        # add c++ directives and remove rosie directives
        nwfl = "#ifndef _"+name.capitalize()+"_\n#define _"+name.capitalize()+"_\n"+nwfl+"\n#endif"
        nwfl = re.sub(r"mode header",r"",nwfl)
    # add includes
    for i in hdrs:
        nwfl = "#include <"+i+".hxx>\n"+nwfl
    for i in hxx:
        nwfl = "#include \""+i+".hxx\"\n"+nwfl
    nwfl = "#include<vector>\n"+nwfl
    return [nwfl,ishdr]