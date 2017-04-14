#The main function for the in-class assignment
import os
from parse import parse_tm

def main():
    expath = os.path.join(os.path.dirname(__file__), "tm.example")
    tm = parse_tm(expath)
    tm.compute_string("abbb")

if __name__ == "__main__":
    main()
