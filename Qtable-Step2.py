from Cube import *
from Scramble_Functions_Step1and2_2x2 import *
import numpy as np


import pickle

import time
import random
from Rtables_EO_andStep2 import *
from testing import *

#2 qtables qCO, qME


EPISODES = 20000000
epsilon = 0.5
EPS_DECAY = 0.9999
SHOW_EVERY = 1000

LEARNING_RATE = 0.1
DISCOUNT = 0.95


start_q2_table1 = "3x3_tables/q2-table1.pickle"
start_q2_table2 = "3x3_tables/q2-table2.pickle"
start_q2_table3 = "3x3_tables/q2-table3.pickle"




cube_2 = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0])
choose = ["B", "U2", "Bi", "D2", "B2", "U2", "L2", "Fi", "D2", "R2", "F2", "R2", "L", "F", "R2", "F2", "D", "Fi", "Li", "B2", "R", "Bi", "L2", "F"]


#print(R_table[1])

#To differentiate them, we use the index of the corner orientations
def state_table(co):
    if 0 <= co < 729:
        #print("table1")
        return Step2_table1

    elif 729 <= co < 1458:
        #print("table2")
        return Step2_table2
    else:
        #print("table3")
        return Step2_table3

def state_table_reverse(co):
    if 0 <= co < 729:
        #print("table1")
        return Step2_table1_reverse

    elif 729 <= co < 1458:
        #print("table2")
        return Step2_table2_reverse
    else:
        #print("table3")
        return Step2_table3_reverse


def reward_table(co):
    if 0 <= co < 729:
        return R2_table_1

    elif 729 <= co < 1458:
        return R2_table_2
    else:
        return R2_table_3



if start_q2_table1 is None:

    #q_table = {}
    #create a matrix of the dimensions given, with all entries equal to 0
    q2_table1 = np.zeros(shape = (729*495, 14)) #5000000
    
else:
    with open(start_q2_table1, "rb") as f:
        q2_table1 = pickle.load(f)

if start_q2_table2 is None:

    #q_table = {}
    q2_table2 = np.zeros(shape = (729*495, 14))
    
else:
    with open(start_q2_table2, "rb") as f:
        q2_table2 = pickle.load(f)


if start_q2_table3 is None:

    #q_table = {}
    q2_table3 = np.zeros(shape = (729*495, 14))

else:
    with open(start_q2_table3, "rb") as f:
        q2_table3 = pickle.load(f)


def q_table(co):
    if 0 <= co < 729:
        return q2_table1

    elif 729 <= co < 1458:
        return q2_table2
    else:
        return q2_table3


cube_2.scramble_read(choose)

CO_number = CO_table_reverse[list_in_str(cube_2.v)]

table = state_table(CO_number)

for key, state in table.items():
    if state[0] == cube_2.v and state[1] == cube_2.MDE_coordinates:
        obs = key



initial_state = obs

def available_actions(state, co):

    #use the function to choose which reward table we need to use.
    current_state_row = reward_table(co)[state,]

    av_act = np.nonzero(current_state_row >= 0)[0]
    return av_act

# Get available actions in the current state
available_act = available_actions(initial_state, CO_number)
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
def update(current_state, action, gamma, co_num):
    
    #compute next state
    current = list(state_table(co_num)[current_state])
    cube_2.v = current[0] #corner orientation
    cube_2.MDE_coordinates = current[1] #edge permutation

    #take the index of the corner orientation
    CO_number = CO_table_reverse[list_in_str(cube_2.v)]
    
    #apply action to next move
    chosen_move = [cube_2.moves2[action]]
    cube_2.scramble_read(chosen_move)

    CO_number_next = CO_table_reverse[list_in_str(cube_2.v)]
 
    state_str = list_in_str(cube_2.v) + list_in_str(cube_2.MDE_coordinates)

    #choose the correct reverse table
    table = state_table_reverse(CO_number_next)  

    #finds the next state
    next_state = table[state_str]

    max_index = np.nonzero(q_table(CO_number_next)[next_state] == np.max(q_table(CO_number_next)[next_state]))[0]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
        
    else:
        max_index = int(max_index)
        
    max_value = q_table(CO_number_next)[next_state, max_index]
    
    # Q learning formula
    q_table(CO_number)[current_state, action] = reward_table(CO_number)[current_state, action] + gamma * max_value



# Update Q matrix
update(initial_state,action,LEARNING_RATE, CO_number)

# Train over 30 000 iterations. (Re-iterate the process above).

print(f"Train q-table over {EPISODES} iterations")

for i in range(EPISODES):
    current_state = np.random.randint(0, 729*495)
    random_co = np.random.randint(0, 2187)
    available_act = available_actions(current_state, random_co)
    
    action = sample_next_action(available_act)
   
    update(current_state, action, LEARNING_RATE, random_co)

  
# Normalize the "trained" Q matrix
print("Trained Q matrix 1:")
print(q2_table1)
print(q2_table2)
print(q2_table3)


with open(f"3x3_tables/q2-table3.pickle", "wb") as f:
    pickle.dump(q2_table3, f)

with open(f"3x3_tables/q2-table2.pickle", "wb") as f:
    pickle.dump(q2_table2, f)

with open(f"3x3_tables/q2-table1.pickle", "wb") as f:
    pickle.dump(q2_table1, f)
