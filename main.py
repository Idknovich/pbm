try:
    import core
except:
    from .core import execute
    
def execute(byte, debug=False):
    core.execute(byte, debug)

if __name__=="__main__":
    program=b"\x023\x00\x035\x00\x0802\x00\x01Works!\x00\x04\x00\xff\x00\x01Anyway...\x00\x04"
    execute(program, True)
