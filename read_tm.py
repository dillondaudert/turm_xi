#Read a Turing Machine transition table, return a TM object
import csv
import os
from pprint import pprint

from turm import Computer, State

def read_tm(t_file: str):
    """Parse a transition table from a file."""

    #TM attributes
    tape_alpha = set()
    in_alpha = set()
    states = set()

    with open(t_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        start_in, finals_in = next(reader)
        start_in = start_in.strip(' ')
        finals_in = [s.strip(' ') for s in finals_in.split(",")]

        #Add start and final states to the set of states
        start_state = State(name=start_in, start=True,
                            final= True if start_in in set(finals_in) else False)
        states.add(start_state)

        for f_state in finals_in:
            if f_state == start_in:
                continue

            states.add(State(name=f_state, start=False, final=True))

        pprint(states.__dict__)


        transition_table = dict()

        alpharow = next(reader)
        alpha = [letter.strip(' ') for letter in alpharow]

        #Add the input alphabet and "B" to the tape alphabet
        for ch in alpha[1:]:
            tape_alpha.add(ch)

        print(tape_alpha)

        print("--")
        for row in reader:
            #Transition: (row[0],alpha[i]) = row[i]

            state_in = row[0].strip(' ')
            for i in range(1,len(row)):
                print("(%s, %s) -> %s; " % (row[0], alpha[i], row[i]))
            print("")

if __name__ == "__main__":
    ex = os.path.join(os.path.dirname(__file__), "tm.example")
    read_tm(ex)
