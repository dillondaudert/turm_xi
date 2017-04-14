#Read a Turing Machine transition table, return a TM object
import csv
import os
from pprint import pprint

from turm import Computer, State
from err import ParseError

DEBUG = True

def read_tm(t_file: str):
    """Parse a transition table from a file."""

    with open(t_file, 'r') as csvfile:

        reader = csv.reader(csvfile, delimiter='|')
        columns = next(reader)
        inputs = [[letter.strip(' ') for letter in col.split(',')] for col in columns[1:]]
        print(inputs)
        print("--")

        states = set()
        state_trans = dict()
        row1 = next(reader)
        #Create the start state from the first row
        start_state = _parse_state(row1, True)
        print(start_state.name, start_state.start, start_state.final)

        states.add(start_state)
        state_trans[start_state] = row1[1:]

def _parse_transition(t_cell:str):
    """Parse out the interior elements of a transition table cell."""
    t_cell_list = t_cell.split(';')
    out_state = t_cell_list[0].strip(' ')
    #If no transition defined here
    if out_state == "-":
        return None
    #Else build the tuple
    out_tracks = [letter.strip(' ') for letter in t_cell_list[1].split(',')]
    out_actions = [act.strip(' ') for act in t_cell_list[2].split(',')]

    #Assert we have an action for each track
    assert len(out_tracks) == len(out_actions)

    return (out_state, out_tracks, out_actions)



def _parse_state(row_state: str,
                 start: bool):
    """Expect an input of "state,(N/F)"
    Convert into a State object."""

    row_list = row_state.split(',')
    if len(row_list) != 2:
        raise ParseError

    name=row_list[0].strip(' ')
    fin=row_list[1].strip(' ')

    if (fin not in ["F", "N"]):
        raise ParseError

    state = State(name=name, start=start, final=True if fin == "F" else False)

    if DEBUG:
        print("Creating State: (%s,%s,%s)\n" % (name, start, fin))

    return state




if __name__ == "__main__":
    ex = os.path.join(os.path.dirname(__file__), "tm.example")
    read_tm(ex)
