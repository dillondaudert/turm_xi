#Read a Turing Machine transition table, return a TM object
import csv
import os
from copy import deepcopy

from turm import Computer, State
from err import ParseError

DEBUG = False

def parse_tm(t_file: str):
    """Parse a transition table from a file.
    See the examples for syntax.
    At the moment, two strings to parse are expected in the input file."""

    with open(t_file, 'r') as csvfile:

        reader = csv.reader(csvfile, delimiter='|')
        #Get the symbol mappings
        symbols = [symbol.split(':') for symbol in next(reader)]
        symbol_map = dict()
        for s in symbols:
            symbol_map[s[0].strip(' ')] = [let.strip(' ') for let in s[1].split(',')]

        #Get the transition columns
        columns = next(reader)
        inputs = [[letter.strip(' ') for letter in col.split(',')] for col in columns[1:]]

        #Record number of tracks
        num_tracks = len(inputs[0])

        states = set()
        state_map = dict()
        trans_map = dict()
        row1 = next(reader)
        #Create the start state from the first row
        start_state = _parse_state(row1[0], True)
        states.add(start_state)
        trans_map[start_state.name] = [_parse_transition(trans) for trans in row1[1:]]
        state_map[start_state.name] = start_state

        for row in reader:
            if row[0] == "-":
                break
            new_state = _parse_state(row[0], False)
            trans_map[new_state.name] = [_parse_transition(trans) for trans in row[1:]]
            states.add(new_state)
            state_map[new_state.name] = new_state
        #Get the two strings to compute
        str1 = next(reader)[0]
        str2 = next(reader)[0]
        assert type(str1) == str
        assert type(str2) == str

        #Build transition function map
        trfunc = _create_transition_function(state_map, trans_map, inputs, symbol_map)
        #Create alphabet set
        alpha = set()
        [[alpha.add(letter) for letter in col] for col in inputs]

    return (Computer(states=states, start_st=start_state, alpha=alpha,
                    trans_table=trfunc, num_tracks=num_tracks), [str1, str2])

def _create_transition_function(state_map: dict,
                                trans_map: dict,
                                inputs: list,
                                symbol_map: dict):
    """Return a dictionary mapping (state, [input_symbols]) to
    (state, [output_symbols], [output_actions])"""

    num_tracks = len(inputs[0])
    trfunc = dict()
    for key in trans_map:
        in_state = state_map[key]
        t_cell = trans_map[key]
        for i, out in enumerate(t_cell):
            if len(out) < 3:
                continue

            if (len(out[1]) != num_tracks or len(out[2]) != num_tracks):
                print("Invalid transition defined: %s,%s\n" % (out[1], out[2]))
                raise ParseError

            #Do the mapping of (symbol) : {alphabet} here


            #Map symbols to the actual alphabet, create transitions
            out_state = state_map[out[0]]

            #Create initial transition with no swapped characters
            t_list = [(inputs[i], out[1])]
            t_list_new = list()

            for symbol in symbol_map:
                for transition in t_list:
                    #If the transition has a replaceable symbol
                    if symbol in transition[0] or symbol in transition[1]:
                        for char in symbol_map[symbol]:
                            #Replace all instances of 'symbol' with 'char' in transition
                            new_transition = deepcopy(transition)
                            for i, in_sym in enumerate(new_transition[0]):
                                if in_sym == symbol:
                                    new_transition[0][i] = char

                            for i, out_sym in enumerate(new_transition[1]):
                                if out_sym == symbol:
                                    new_transition[1][i] = char
                            t_list_new.append(new_transition)
                    else:
                        t_list_new.append(deepcopy(transition))

                t_list = t_list_new
                t_list_new = list()


            for inp, outp in t_list:
                #Create a transition for each pair
                new_input = (in_state, tuple(inp))
                new_output = (out_state, outp, out[2])
                trfunc[new_input] = new_output


    return trfunc



def _parse_transition(t_cell:str):
    """Parse out the interior elements of a transition table cell."""
    t_cell_list = t_cell.split(';')

    out_state = t_cell_list[0].strip(' ')
    #If no transition defined here
    if out_state == "-":
        return ("")

    if len(t_cell_list) != 3:
        raise ParseError


    #Else build the tuple
    out_tracks = [letter.strip(' ') for letter in t_cell_list[1].split(',')]
    out_actions = [act.strip(' ') for act in t_cell_list[2].split(',')]
    for action in out_actions:
        if action not in ["L", "R", "S"]:
            raise ParseError

    #Assert we have an action for each track

    if len(out_tracks) != len(out_actions):
        raise ParseError

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

    return state




if __name__ == "__main__":
    ex = os.path.join(os.path.dirname(__file__), "tm.example")
    parse_tm(ex)
