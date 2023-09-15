try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x15S\x00\01Hello\x00\x04\x00\xff\x00\x16S"
    core.execute(program, True)
