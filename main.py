#The main function for the in-class assignment
import os
from parse import parse_tm

def main():
    expath = os.path.join(os.path.dirname(__file__),"examples")
    for example in os.listdir(expath):
        print("Example: %s" % example)
        tm, strings = parse_tm(os.path.join(expath, example))
        for string in strings:
            tm.compute_string(string)

        print()

if __name__ == "__main__":
    main()
