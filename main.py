try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x0c\x00\x0avar\x00\x10var\x00\x0612\x00\x04"
    core.execute(program, True)
