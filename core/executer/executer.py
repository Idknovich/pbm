from ..lexer import lex
from .coms import *

def execute(byte_code, debug=False):
    #setup
    reg1=""
    reg2=""
    reg3=""
    is_loop=False
    #
    steps=""
    
    c=getb()
    byte_code=lex(byte_code)
    codee=""""""
   
    for i in byte_code:#translate

        if i["com"]=="0xfd":
            is_loop=True
            continue
        
        com=c[i["com"]]
        
        
        if i["com"]=="0xff":
            steps=steps[:-1]
            continue
        
        arg=i["params"].decode("utf-8")

        if i["com"]=="0x8":
            
            if not arg[0]==b"\x01":
                thing=com.replace("arg", "not")
                
            codee+=steps+thing+"\n"
            steps+=" "
            continue

        
        com=com.replace("arg", arg)
        
        thing=com.replace("aarg", "\'"+arg+"\'")
        codee+=steps+thing+"\n"

        if ":" in com:
            steps+=" "

    if is_loop:
        print(codee)
        codde=""
        for line in codee.split("\n"):
            codde=codde+" "+line+"\n"
        codee="while True:\n"+codde
        
    if debug:
        print(codee)
        print("")
    
    exec(codee)
