from Cube import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np

import pickle

import time
import random
from Rtables_EO_andStep2 import *

EPISODES = 150000
epsilon = 0.5
EPS_DECAY = 0.9999
SHOW_EVERY = 1000

LEARNING_RATE = 0.1
DISCOUNT = 0.8

start_q_table = "3x3_tables/qEO3table.pickle"

cube_eo = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0])
choose_eo = ["B", "U2", "Bi", "D2", "B2", "U2", "L2", "Fi", "D2", "R2", "F2", "R2", "L", "F", "R2", "F2", "D", "Fi", "Li", "B2"]

if start_q_table is None:

    #q_table = {}
    q_table = np.zeros(shape = (2048, 2048))
    """ for i in range(2048):
        q_table[i]= [0 for i in range(18)] """
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

cube_eo.scramble_read(choose_eo)

string_EO = list_in_str(cube_REO_v2.w)

initial_state = EO_table_reverse[string_EO]


def available_actions(state):
    current_state_row = REO_table_v2[state,]
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
    

    max_index = np.nonzero(q_table[action] == np.max(q_table[action]))[0]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
        
    else:
        max_index = int(max_index)
        
    max_value = q_table[action, max_index]
    
    
    # Q learning formula
    q_table[current_state, action] = REO_table_v2[current_state, action] + gamma * max_value
    

# Update Q matrix
update(initial_state,action, LEARNING_RATE)

# Train over 200 000 iterations. (Re-iterate the process above).

print(f"Train q-table over {EPISODES} iterations")

for i in range(EPISODES):
    current_state = np.random.randint(0, int(q_table.shape[0]))
    available_act = available_actions(current_state)
    
    action = sample_next_action(available_act)
    update(current_state, action, LEARNING_RATE)

with open(f"3x3_tables/qEO3table.pickle", "wb") as f:
    pickle.dump(q_table, f)   
# Normalize the "trained" Q matrix
print("Trained Q matrix:")
print(q_table)