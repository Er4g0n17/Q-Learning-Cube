from Cube2x2 import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np


import pickle

import time
import random
from Rtable2x2 import *


#2 qtables qCO, qME


EPISODES = 250000

epsilon = 0.5
EPS_DECAY = 0.9999
SHOW_EVERY = 1000

LEARNING_RATE = 0.1


start_qCO_table = "2x2_tables/qCOtable2x2.pickle"




cube_2 = Cube2x2(Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7])
step2_start = ["B", "U2", "Bi", "D2", "B2", "U2", "L2", "Fi", "D2", "R2", "F2", "R2", "L", "F", "R2", "F2", "D", "Fi", "Li", "B2", "R", "Bi", "L2", "F"]

if start_qCO_table is None:

    #q_table = {}
    qCO_table = np.zeros(shape = (2187, 2187))
    """ for i in range(2048):
        q_table[i]= [0 for i in range(18)] """
else:
    with open(start_qCO_table, "rb") as f:
        qCO_table = pickle.load(f)



cube_2.scramble_read(step2_start)

string_CO = list_in_str(cube_2.v)

initial_state_CO = CO_table_reverse[string_CO]


def available_actions_CO(state):
    current_state_row_co = R_tableCO[state,]
    av_act_co = np.nonzero(current_state_row_co >= 0)[0]
    return av_act_co

# Get available actions in the current state
available_act_CO = available_actions_CO(initial_state_CO)


# This function chooses at random which action to be performed within the range 
# of all the available actions.
def sample_next_action(available_actions_range):
    #print(available_actions_range)
    next_action = int(np.random.choice(available_actions_range))
    return next_action

# Sample next action to be performed
act_CO = sample_next_action(available_act_CO)


# This function updates the Q matrix according to the path selected and the Q 
# learning algorithm
def update(current_state_CO, action_CO, gamma):
    

    max_index_CO = np.nonzero(qCO_table[action_CO] == np.max(qCO_table[action_CO]))[0]
    
    if max_index_CO.shape[0] > 1:
        max_index_CO = int(np.random.choice(max_index_CO, size = 1))
        
    else:
        max_index_CO = int(max_index_CO)
        
    max_value_CO = qCO_table[action_CO, max_index_CO]
    
    
    # Q learning formula
    qCO_table[current_state_CO, action_CO] = R_tableCO[current_state_CO, action_CO] + gamma * max_value_CO

    

# Update Q matrix
update(initial_state_CO, act_CO, LEARNING_RATE)

# Train over 30 000 iterations. (Re-iterate the process above).

print(f"Train q-table over {EPISODES} iterations")

for i in range(EPISODES):
    current_state_CO = np.random.randint(0, int(qCO_table.shape[0]))

    available_act_CO = available_actions_CO(current_state_CO)
    
    action_CO = sample_next_action(available_act_CO)
    update(current_state_CO, action_CO, LEARNING_RATE)


with open(f"2x2_tables/qCOtable2x2.pickle", "wb") as f:
    pickle.dump(qCO_table, f)