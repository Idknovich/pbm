try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x012\x00\x022\x00\x12\x00\x07+\x00\x04"
    core.execute(program, True)
