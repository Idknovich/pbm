try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x1c5\x00\x01Wait end\x00\x04"
    core.execute(program, True)
