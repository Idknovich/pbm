try:
    from .core import execute

except:
    import core
    

if __name__=="__main__":
<<<<<<< HEAD
    program=b"\x0e\x00\x0avar\x00\x03hi\x00\x0fvar\x00\x0bvar\x00\x0613\x00\x04"
    core.execute(program, True)
=======
    program=b"\x0c\x00\x0613\x00\x04"
    execute(program, True)
>>>>>>> 92f3d9876962829662e467222a0c9cd9d2c31bf3
