from ..lexer import lex
from .coms import *

def execute(byte_code, debug=False):
    #setup
    reg1=""
    reg2=""
    reg3=""
    #
    c=getb()
    byte_code=lex(byte_code)
    codee=""""""
    
    for i in byte_code:#translate
        arg=i["params"].decode("utf-8")
        com=c.get(i["com"])
        thing=com.replace("arg", "'"+arg+"'")
        codee+=thing+"\n"

    if debug:
        print(codee)
        print("")
    exec(codee)
