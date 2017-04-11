#Turing Machine Machine object and support functions
import numpy as np
import collections

MachineState = collections.namedtuple('MachineState', ['current_state', 'track_heads'])

class Computer():

    num_tracks = 0
    states = None
    input_alphabet = None
    tape_alphabet = None
    transition_table = None
    start_state = None
    self.tracks = None

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

        current_state = self.start_state,
        track_heads = [0 for i in range(num_tracks)])
        #Initialize the tracks
        self.tracks = [["B" for i in range(len(w)+2)] for j in range(self.num_tracks)]

        for i in range(1,len(w)+1)
            self.tracks[0][i] = list(w)[i-1]
        print(self.tracks)

    def transition(self,
                   current_state: State,
                   track_heads: list):
        """Transition the machine from one state to another,
        performing all necessary computations."""

        track_state = [self.tracks[i][j] for i,j in enumerate(track_heads)]
        new_state, new_track_state, actions = self.transition_table[(current_state,
                                                                     track_state)]

        #Modify the tracks
        for track in range(self.num_tracks):
            self.tracks[track][track_heads[track]] = new_track_state[track]

        #Move the track heads
        for i, action in enumerate(actions):
            if action == "L":
                if track_heads[i] > 0:
                    track_heads[i] -= 1
                else:
                    #raise TrackOverflowError
                    print("Track head %d less than 0!" % i)
                    quit()
            else if action == "R":
                track_heads[i] += 1
                if track_heads[i] >= len(self.tracks[i]):
                    #Append a blank to extend the track
                    self.tracks[i].append("B")

        return (new_state, track_heads)



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
