#Turing Machine Machine object and support functions

class Computer():

    num_tracks = 0
    states = None
    input_alphabet = None
    tape_alphabet = None
    transition_table = None
    start_state = None


    def __init__(self,
                 num_tracks: int,
                 states: set,
                 in_alpha: set,
                 tp_alpha: set,
                 start_st: State,
                 trans_table: dict):
        self.states = states
        self.input_alphabet = in_alpha
        self.tape_alphabet = tp_alpha
        self.transition_table = trans_table
        self.num_tracks = num_tracks
        self.start_state = start_st

    def compute_string(self,
                       w: str):
        """Perform a computation of the string 'w', accept or reject"""


class State():
    name = None
    start = False
    final = False
    def __init__(self,
                 name: str,
                 start: bool,
                 final: bool):
        self.name = name
        self.start = start
        self.final = final
