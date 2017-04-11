#The specs for the Turing Machine simulator project

1. Simulate a Turing Machine acceptor M
    > Read a Turing Machine spec from a file
    > Build the TM object
    > Read strings from a file, accept or reject string by final state

2. The Turing Machine can be
    > One-track, one-way
    > Multi-track, one-way

Input/Output
-
Read the transition table from a file
    > Format:
    > TM: <name>
    > <start_state> | <final_state>,<final_state>,<final_state>,...
    > delta|   <letter>| <letter>| <letter>| ...
    > <state>| <state>,<letter>,<LRS>; <state>,<letter>,<LRS>; ...| ...
    > <state>| ...

Read strings from a file
Print whether a string is accepted or rejected


Turing Machine Simulator
-
A five-tuple: (States, Input_Set, Tape_Set, Transition_Function, Start_State)
States
    > A set of states
    > Final/start

Input_Set
    > A set of input symbols, a subset of the tape alphabet (minus the blank symbol)

Tape_Set
    > A set of tape symbols, with an additional blank symbol

Transition_Function
    > A function mapping (state, [tape_0 symbol, tape_1 symbol, ..., tape_n symbol])
    > to (new state, [(new tape_0 symbol, L/R/S), ..., (new tape_n symbol, L/R/S)])


    Tracks:
    [B, i, n, p, u, t, B, ...]
    [B, B, B, ...]
    [B, a, b, B, ...]
    ...

    Machine State = CurrentState, Tracks[1, 0, 3, ...]

    Transition Function:
        Current Machine State = [1, 2, ...]
        New State, Actions = TransitionTable(State)
    Action: (new symbol, +1/0/-1)
    UpdateState(Actions):
        for track, action in enumerate(Actions):


