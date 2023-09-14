try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x01Hello, \x00\x02World!\x00\x11\x00\x04"
    core.execute(program, True)
