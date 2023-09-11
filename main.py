try:
    import core
except:
    from .core import execute
    
def execute(byte, debug=False):
    core.execute(byte, debug)

if __name__=="__main__":
    program=b"\x0252\x00\x0152\x00\x07\x00\x0621\x00\x01Num: \x00\x05"
    execute(program, True)
