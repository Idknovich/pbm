try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
    program=b"\x0e\x00\x0avar\x00\x03hi\x00\x0fvar\x00\x0bvar\x00\x0613\x00\x04"
    core.execute(program, True)
