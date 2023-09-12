try:
    import core
except:
    from .core import execute
    
def execute(byte, debug=False):
    core.execute(byte, debug)

if __name__=="__main__":
    program=b"\x0155\x00\x0255\x00\x07/\x00\x04"
    execute(program, True)
