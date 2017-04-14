#The main function for the in-class assignment
import os
from parse import parse_tm

def main():
    expath = os.path.join(os.path.dirname(__file__), "examples", "tm.8_2_2")
    tm, strings = parse_tm(expath)
    for string in strings:
        tm.compute_string(string)
    quit()

    expath = os.path.join(os.path.dirname(__file__),"examples")
    for example in os.listdir(expath):
        tm, strings = parse_tm(expath)
        for string in strings:
            tm.compute_string(string)

if __name__ == "__main__":
    main()
