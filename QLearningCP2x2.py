from Cube2x2 import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np
import pickle
import time
import random
from Rtable2x2 import *


def qCP2x2(scramble):
    start_qCP_table = "2x2_tables\qCPtable2x2.pickle"


    if start_qCP_table is None:
        pass
    else:
        with open(start_qCP_table, "rb") as f:
            qCP_table = pickle.load(f)


    new_cube = Cube2x2(Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7])

    #scramble
    CP_to_solve =  scramble
    
    #apply the scramble
    new_cube.scramble_read(CP_to_solve)
    print(new_cube.cp)
    remember_cp = tuple(new_cube.cp)

    for key, cp in CP_table.items():
        if list(cp) == new_cube.cp:
            obs = key

    current_state = obs
    steps = []
    #qtable = {state : (next_state, value)}, now it is qtable = {state}
    counter3 = 0

    #iterate until the goal state is reached
    while current_state not in [0, 5889, 8427, 11536, 15138, 17137, 20508, 23182, 28783, 40319] and counter3 < 200:

        next_step_index = np.nonzero(qCP_table[current_state] == np.max(qCP_table[current_state]))[0]
        
        #if mutliple next state choose one randomly
        if next_step_index.shape[0] > 1:
            next_step_index = int(np.random.choice(next_step_index, size = 1))
        else:
            next_step_index = int(next_step_index)
        
        steps.append(next_step_index)

        #apply the chosen move on the cube
        chosen_move = [new_cube.moves2[next_step_index]]
        new_cube.scramble_read(chosen_move)


        for key, cp in CP_table.items():
            if list(cp) == new_cube.cp:
                next_state = key

        current_state = next_state
        print("searching")
        counter3 += 1

    # Print selected sequence of steps
    print("Selected path:")
    print(steps)

    cp_solution = []

    for move in steps:

        cp_solution.append(new_cube.moves2[move])

    print(f"CP solution for scramble {CP_to_solve} and EO {remember_cp}:")
    print(cp_solution)

    print("final cp is ", new_cube.cp)
    return cp_solution