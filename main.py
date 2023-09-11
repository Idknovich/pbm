try:
    import core
except:
    from .core import execute
    
def execute(byte, debug=False):
    core.execute(byte, debug)

if __name__=="__main__":
    program=b"\x09s\x00\x01s\x00\x0aHi\x00\x0bs\x00\x0613\x00\x04"
    execute(program, True)
