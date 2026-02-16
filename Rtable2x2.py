from Cube2x2 import *
import numpy as np
import pickle
import time
import random
import itertools

#create lists and dictonary that contains all possible corner orientations
COs = []

for corner_o in range(6561):
    str_tern = np.base_repr(corner_o, base = 3)
    list_tern = list(str_tern)
    sum_bit = 0
    for bit in list_tern:
        sum_bit += int(bit)

    if sum_bit % 3 == 0:
        COs.append(list_tern)

for terns in COs:
    counter5 = 0
    for b in terns:
        terns[counter5] = int(b)
        counter5 += 1

counter4 = 0    
for terns in COs:
    while len(terns) < 8:
        terns = [0] + terns
    
    COs[counter4] = terns
    counter4 += 1

CO_table = {}
co_n = 0
nbCo = {}
for co in COs:

    CO_table[co_n] = tuple(co)
    co_n += 1
co_n2 = 0

str_CO = []

for terns in COs:
    str_CO.append(list_in_str(terns))

CO_table_reverse = {}

co_n3 = 0
for co in str_CO:

    CO_table_reverse[co] = co_n3
    co_n3 += 1


cube = Cube2x2(Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7])


start_RtableCO = "2x2_tables/R-tableCO2x2.pickle"

#create the R-table, same method than for edge orientation for 3x3
if start_RtableCO is None:
    R_tableCO = np.zeros(shape = (2187, 2187))
    for x in range(2187):
        for y in range(2187):
            R_tableCO[x][y] = -1
    
    for x in range(2187):
        for move in cube.moves:
            remember_co = R_tableCO[x]
            cube.v = list(CO_table[x])
            cube.scramble_read([move])

            string_CO = list_in_str(cube.v)

            y = CO_table_reverse[string_CO]

            if cube.number_NCO() == 0:
                R_tableCO[x][y] = 100
            else:
                R_tableCO[x][y] = 0
            
            """ elif cube_RCO.number_NCO() == 4:
            RCO_table[x][y] = 50
            elif cube_RCO.number_NCO() < number_NCO2(remember_co):
            RCO_table[x][y] = 25
            elif list(remember_co) == cube_RCO.v: 
            RCO_table[x][y] = 1 """

else:
    with open(start_RtableCO, "rb") as f:
        R_tableCO = pickle.load(f)

with open("2x2_tables/R-tableCO2x2.pickle", "wb") as f:
    pickle.dump(R_tableCO, f)

CPs = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7]))


CP_table = {}

counter = 0

for cp in CPs:
    CP_table[counter] = cp
    counter += 1

CP_table_reverse = {}

counter = 0
for cp in CPs:

    CP_table_reverse[list_in_str(cp)] = counter
    counter += 1

start_RtableCP = "2x2_tables/R-tableCP2x2.pickle"

#create the reward table, same method used for step 2 on 3x3
if start_RtableCP is None:

    R_tableCP = np.zeros(shape= (40320, 10))
    

    for x in range(40320):

        for move in range(10):

            remember_cp = R_tableCP[x]
            cube.cp = list(CP_table[x])
            cube.scramble_read([cube.moves2[move]])

            if cube.cp == [0, 1, 2, 3, 4, 5, 6, 7] or cube.cp == [1, 2, 3, 0, 5, 6, 7, 4] or cube.cp == [3, 0, 1, 2, 7, 4, 5, 6] or cube.cp == [4, 5, 1, 0, 7, 6, 2, 3] or cube.cp == [3, 2, 6, 7, 0, 1, 5, 4] or cube.cp == [2, 3, 0, 1, 6, 7, 4, 5] or cube.cp == [7, 6, 5, 4, 3, 2, 1, 0] or cube.cp == [5, 4, 7, 6, 1, 0, 3, 2] or cube.cp == [4, 0, 3, 7, 5, 1, 2, 6] or cube.cp == [1, 5, 6, 2, 0, 4, 7, 3]:
                R_tableCP[x][move] = 100
            else:
                R_tableCP[x][move] = 0

else:
    with open(start_RtableCP, "rb") as f:
        R_tableCP = pickle.load(f)

with open("2x2_tables/R-tableCP2x2.pickle", "wb") as f:
    pickle.dump(R_tableCP, f)