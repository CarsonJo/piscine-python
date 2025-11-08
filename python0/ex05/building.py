import sys
"""Take a string as argument and print the number of character"""


def start() -> str:
    """check argument"""
    sys.tracebacklimit = 0
    if len(sys.argv) > 2:
        assert False, "more than one argument is provided"
    elif len(sys.argv) < 2:
        print("what is the text to count?")
        ret: str = sys.stdin.read()
        return ret
    return sys.argv[1]


def main():
    upper: int = 0
    lower: int = 0
    punctuation: int = 0
    space: int = 0
    digits: int = 0
    my_str: str = start()
    for i in my_str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace() or i == '\n':
            space += 1
        elif i.isdigit():
            digits += 1
        elif i.isprintable():
            punctuation += 1
    print("The text contain ", end='')
    print(upper + lower + punctuation + space + digits, "character :")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(space, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    main()
