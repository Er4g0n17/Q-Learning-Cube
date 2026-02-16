#Different approach of using q-learning to solve edge orientation

from Cube2x2 import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np


import pickle

import time
import random
from Rtable2x2 import *

EPISODES = 500000

epsilon = 0.5
EPS_DECAY = 0.9999
SHOW_EVERY = 1000

start_qCP_table = "2x2_tables/qCPtable2x2.pickle"
LEARNING_RATE = 0.1
DISCOUNT = 0.95

cube_cp = Cube2x2(Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7])
choose_cp = ["F", "R2", "Ui", "Ri", "Fi", "U", "F", "R2", "F2"]

#print(R_table[1])

if start_qCP_table is None:

    #q_table = {}
    qCP_table = np.zeros(shape = (40320, 10))
    
else:
    with open(start_qCP_table, "rb") as f:
        qCP_table = pickle.load(f)

cube_cp.scramble_read(choose_cp)

for key, cp in CP_table.items():
    if list(cp) == cube_cp.cp:
        obs = key

initial_state = obs

def available_actions(state):
    current_state_row = R_tableCP[state,]
    av_act = np.nonzero(current_state_row >= 0)[0]
    return av_act

# Get available actions in the current state
available_act = available_actions(initial_state)
#print(available_act)

# This function chooses at random which action to be performed within the range 
# of all the available actions.
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_actions_range))
    return next_action

# Sample next action to be performed
action = sample_next_action(available_act)

# This function updates the Q matrix according to the path selected and the Q 
# learning algorithm
def update(current_state, action, gamma):
    
    #compute next state
    current_cp = list(CP_table[current_state])
    cube_cp.cp = current_cp
    
    #apply action to next move
    choosed_move = [cube_cp.moves2[action]]
    cube_cp.scramble_read(choosed_move)
    
    for key, cp in CP_table.items():
        if list(cp) == cube_cp.cp:
            next_state = key
    

    max_index = np.nonzero(qCP_table[next_state] == np.max(qCP_table[next_state]))[0]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
        
    else:
        max_index = int(max_index)
        
    max_value = qCP_table[next_state, max_index]
    
    
    # Q learning formula
    qCP_table[current_state, action] = R_tableCP[current_state, action] + gamma * max_value
    

# Update Q matrix
update(initial_state,action,LEARNING_RATE)

# Train over 30 000 iterations. (Re-iterate the process above).

print(f"Train q-table over {EPISODES} iterations")

for i in range(EPISODES):
    current_state = np.random.randint(0, int(qCP_table.shape[0]))
    available_act = available_actions(current_state)
    
    action = sample_next_action(available_act)
    update(current_state, action, LEARNING_RATE)

with open(f"2x2_tables/qCPtable2x2.pickle", "wb") as f:
    pickle.dump(qCP_table, f)   
# Normalize the "trained" Q matrix
print("Trained Q matrix:")
print(qCP_table)
