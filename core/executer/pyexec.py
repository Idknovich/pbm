import subprocess

def execute(code):
    subprocess.run(["pypy3", "-c", code])
