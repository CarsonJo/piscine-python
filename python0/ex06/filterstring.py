import sys


def start():
    sys.tracebacklimit = 0
    if len(sys.argv) != 3:
        assert False, "the arguments are bad"
    try:
        int(sys.argv[2])
    except Exception:
        assert False, "the arguments are bad"


def filterstring(string: str, size: int) -> list:
    arr = [x for x in (lambda s: s.split())(string) if len(x) > size]
    for i in arr:
        print(i)
    return arr


def main():
    start()
    filterstring(sys.argv[1], int(sys.argv[2]))


if (__name__ == "__main__"):
    main()
