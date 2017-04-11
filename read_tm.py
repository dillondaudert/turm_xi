#Read a Turing Machine transition table, return a TM object
import csv
import os

from turm import Computer, State

def read_tm(t_file: str):
    """Parse a transition table from a file."""

    #TM attributes
    tape_alpha = set()
    in_alpha = set()
    states = set()

    with open(t_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        namerow = next(reader)
        print(namerow)
        secondrow = next(reader)
        alpharow = next(reader)
        alpha = [letter.strip(' ') for letter in alpharow]
        print(alpha)
        print("--")
        for row in reader:
            #Transition: (row[0],alpha[i]) = row[i]
            for i in range(1,len(row)):
                print("(%s, %s) -> %s; " % (row[0], alpha[i], row[i]))
            print("")

if __name__ == "__main__":
    ex = os.path.join(os.path.dirname(__file__), "tm.example")
    read_tm(ex)
