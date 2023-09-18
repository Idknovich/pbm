try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x185\x00\x0aX\x00\x10X\x00\x05"
    core.execute(program, True)
