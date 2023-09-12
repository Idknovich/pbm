try:
    import core
except:
    from .core import execute
    
def execute(byte, debug=False):
    core.execute(byte, debug)

if __name__=="__main__":
    program=b"\x03q\x00\x0aQ\x00\x0bQ\x00\x0613\x00\x04"
    execute(program, True)
