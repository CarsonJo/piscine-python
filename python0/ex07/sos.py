import sys
"""sos take a string and transform it into morse code"""


def sos(s: str):
    NESTED_MORSE = {
        # Lettres
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        # Chiffres
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        # Espace
        " ": "/ "
    }
    for i in s:
        print(NESTED_MORSE[i.upper()], end=" ")


def main():
    sys.tracebacklimit = 0
    if (len(sys.argv) != 2):
        assert False, "the arguments are bad"
    for i in sys.argv[1]:
        if (not i.isalnum() and i != ' '):
            assert False, "the arguments are bad"
    sos(sys.argv[1])


if (__name__ == "__main__"):
    main()
