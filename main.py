try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b""
    core.execute(program, True)
