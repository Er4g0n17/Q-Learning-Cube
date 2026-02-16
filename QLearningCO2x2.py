from Cube2x2 import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np
import pickle
import time
import random
from Rtable2x2 import *

def qCO2x2(scramble):

    start_qCO_table = "2x2_tables\qCOtable2x2.pickle"

    if start_qCO_table is None:
        pass
    else:
        with open(start_qCO_table, "rb") as f:
            qCO_table = pickle.load(f)


    new_cube = Cube2x2(Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7])

    #input here a scramble
    choosed_scramble = scramble

    #apply the scramble
    new_cube.scramble_read(choosed_scramble)
    print(new_cube.v)
    remember_co = tuple(new_cube.v)

    #search for state
    for key, co in CO_table.items():
        if list(co) == new_cube.v:
            obs = key

    current_state = obs
    print(current_state)
    #steps = []

    counter3 = 0
    steps = [current_state]

    #iterate until the goal state has been reached
    while current_state != 0 and counter3 < 200:

        next_step_index = np.nonzero(qCO_table[current_state] == np.max(qCO_table[current_state]))[0]
        
        if next_step_index.shape[0] > 1:
            
            next_step_index = int(np.random.choice(next_step_index, size = 1))
            

        else: next_step_index = int(next_step_index)
            
        steps.append(next_step_index)

        current_state = next_step_index
        counter3 += 1

    # Print selected sequence of steps
    print("Selected path:")
    print(steps)

    #This will give in which state the execution went. We either can have directly in the R-table, what move is used using a tuple.


    if steps[-1] == 0:
        print(f"Solution for scramble {choosed_scramble} is:")
        print(steps)
        solution = deduce_moves_from_states_CO2x2(steps)
        print(solution)

    new_cube.scramble_read(solution)
    print(new_cube.v)
    
    return solution



