import sys
import antigravity

def moon():
    try:
        if (len(sys.argv) != 4):
            raise Exception("Usage: geohashing.py 37.421542 -122.085589 \"2005-05-26-10458.68\"")
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), bytes(sys.argv[3], 'utf-8'))
    except Exception as e:
        print (e)

if __name__ == '__main__':
    moon()
