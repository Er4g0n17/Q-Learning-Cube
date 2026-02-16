from Cube import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np
import pickle
import time
import random
from Rtables_EO_andStep2 import *

#Same approach than EO2 but with different reward table.

#Different approach of using q-learning to solve edge orientation
def EO3_solver(scramble):

    start_q_table = "3x3_tables/qEO3table.pickle"

    if start_q_table is None:
        pass
    else:
        with open(start_q_table, "rb") as f:
            q_table = pickle.load(f)

    new_cube = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0])

    #input here a scramble
    EO_to_solve = scramble
    
    new_cube.scramble_read(EO_to_solve)
    #print(new_cube.w)
    remember_eo = tuple(new_cube.w)

    for key, eo in EO_table.items():
        if list(eo) == new_cube.w:
            obs = key

    current_state = obs
    #print(current_state)
    #steps = []

    counter3 = 0
    steps = [current_state]

    #iterate until the goal is reached
    while current_state != 0 and counter3 < 200:

        next_step_index = np.nonzero(q_table[current_state] == np.max(q_table[current_state]))[0]
        
        #if several state choose one randomly
        if next_step_index.shape[0] > 1:
            
            next_step_index = int(np.random.choice(next_step_index, size = 1))
            

        else: next_step_index = int(next_step_index)

        #add the state in the list of steps   
        steps.append(next_step_index)

        current_state = next_step_index
        counter3 += 1

    # Print selected sequence of steps
    print("Selected path:")
    print(steps)

    #This will give in which state the execution went. We either can have directly in the R-table, what move is used using a tuple.

    solution = []

    if steps[-1] == 0:
        print(f"Solution for scramble {scramble} is:")
        solution = deduce_moves_from_states_EO(steps)
        print(deduce_moves_from_states_EO(steps))
    
    return solution


