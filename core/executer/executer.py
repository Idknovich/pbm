from ..lexer import lex
from .coms import *
def execute(byte_code):
    c=getb()
    byte_code=lex(byte_code)
    
    for i in byte_code:
        arg=i["params"]
        com=c[i["com"]]
        exec(com)
        
