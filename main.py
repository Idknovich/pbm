try:
    import core
except:
    from .core import execute
    
def execute(byte):
    core.execute(byte)

if __name__=="__main__":
    program=b"\x01ura\x00\x04"
    execute(program)
