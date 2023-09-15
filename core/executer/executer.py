from ..lexer import lex
from .coms import *
from .pyexec import execute as exec2

def execute(byte_code, debug=False):
    #setup
    reg1=""
    reg2=""
    reg3=""
    
    counter=0
    #
    steps=""
    
    c=getb()
    byte_code=lex(byte_code)
    codee="import sys;sys.set_int_max_str_digits(10000000000)\n"
   
    for i in byte_code:#translate
        try:
            com=c[i["com"]]
        except KeyError:
            counter=str(counter)
            print("invalid byte: "+i["com"]+" in "+counter+" byte")
            exit()
        
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
        codee+=steps+thing+f"#{i['com']} {counter}"+"\n"

        if ":" in com:
            steps+=" "
        counter+=1
        
    if debug:
        print(codee)
        print("")
    
    exec2(codee)
