from local_lib import path
from path import Path

def pathy():
    d = Path('./gg')
    d.mkdir_p()
    d = Path('./gg/op')
    d.touch()
    d.open(mode='w')
    d.write_text("Hello world!")
    print(d.text())

if __name__ == '__main__':
    pathy()
