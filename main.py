try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x0c\x00\x0613\x00\x04"
    execute(program, True)
