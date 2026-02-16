#simplifies a solution by removing 4 consecutives moves
from Cube import *
from Rtables_EO_andStep2 import *
from Rtable2x2 import *
from Cube2x2 import *

#We can also create a function that will find what are the moves done to go from a state to an other.
def deduce_moves_from_states_EO(states):

    test_cube = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0])
    EO_solution = []

    for state_index in range(len(states) - 1):
        print("NEW STATE")
        test_cube.w = list(EO_table[states[state_index]])
        print("EO:", test_cube.w)
        next_state = states[state_index + 1]
        next_state_EO = list(EO_table[next_state])

        for move in test_cube.moves:
            
            test_cube.scramble_read([move])
            
            if test_cube.w == next_state_EO:

                EO_solution.append(move)
                break

            test_cube.w = list(EO_table[states[state_index]])
                
    
    return EO_solution

#iterate through the state giben by q-learning to find which movements have been applied
def deduce_moves_from_states_CO2x2(states):

    test_cube = Cube2x2(Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7])
    CO_solution = []

    for state_index in range(len(states) - 1):
        print("NEW STATE")
        test_cube.v = list(CO_table[states[state_index]])
        print("CO:", test_cube.v)
        next_state = states[state_index + 1]
        next_state_CO = list(CO_table[next_state])

        for move in test_cube.moves:
            
            test_cube.scramble_read([move])
            
            if test_cube.v == next_state_CO:
                print(move)

                CO_solution.append(move)
                break

            test_cube.v = list(CO_table[states[state_index]])
                
    
    return CO_solution

""" def deduce_moves_from_states_Step2(states, scramble):

    test_cube = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0])
    test_cube.scramble_read(scramble)
    Step2_solution = []

    for state_index in range(len(states) - 1):

        remember_v = tuple(test_cube.v)
        remember_me = tuple(test_cube.MDE_coordinates)

        next_state = states[state_index + 1]
        next_state_nco = Step2_table[next_state][0]
        next_state_nme = Step2_table[next_state][1]

        for move in test_cube.moves2:
            
            test_cube.scramble_read([move])
            
            if test_cube.number_ME_in_E() == next_state_nme and test_cube.number_NCO() == next_state_nco:

                Step2_solution.append(move)
                break

            test_cube.v = list(remember_v)
            test_cube.MDE_coordinates = list(remember_me)
     
    
    return Step2_solution """