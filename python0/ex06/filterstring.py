import sys


def start():
    sys.tracebacklimit = 0
    if len(sys.argv) != 3:
        assert(False), "the arguments are bad" 
    try:
        int(sys.argv[2])
    except:
        assert(False), "the arguments are bad"

def filterstring(string: str, size: int) -> list:
    splt = lambda a : a.split()
    arr = [x for x in splt(string) if len(x) > size]
    for i in arr:
        print(i)
    return arr

def main():
    start()
    filterstring(sys.argv[1], int(sys.argv[2]))

if (__name__ == "__main__"):
    main()

