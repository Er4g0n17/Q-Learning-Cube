from Cube import *
import numpy as np
import pickle
import time
import random
import itertools



EOs = []


#length 12, we create binary numbers of length 12
for n in range(4096):
    str_bin = str(bin(n))

    str_bin = str_bin[2:]
    #create a list with the number
    list_bin = list(str_bin)
    sum_bit = 0
    for bit in list_bin:
        sum_bit += int(bit)

    if sum_bit % 2 == 0:
        EOs.append(list_bin)

    
for bins in EOs:
    counter1 = 0
    for b in bins:
        bins[counter1] = int(b)
        counter1 += 1

counter2 = 0    
for bins in EOs:
    while len(bins) < 12:
        bins = [0] + bins
    
    EOs[counter2] = bins
    counter2 += 1

str_EO = []

for bins in EOs:
    str_EO.append(list_in_str(bins))

EO_table = {}
eo_n = 0
nbEo = {}
for eo in EOs:

    EO_table[eo_n] = tuple(eo)
    eo_n += 1


eo_n2 = 0

EO_table_reverse = {}

for eo in str_EO:

    EO_table_reverse[eo] = eo_n2
    eo_n2 += 1


def EO_number(eo):
    for key, eo in EO_table.items():
        if list(eo) == eo:
            number = key
    
    return number

start_REO_table_v2 = "3x3_tables/REO-tablev2.pickle"


cube_REO_v2 = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0])       

if start_REO_table_v2 is None:

    REO_table_v2 = np.zeros(shape = (2048, 2048)) #on 2048 states
    #Set all entries at -1
    #REO_table_v2 = np.matrix([[-1 for i in range(2048)] for j in range(2048)])
    for x in range(2048):
        for y in range(2048):
            REO_table_v2[x][y] = -1
    
    counter_9 = 0
    for x in range(2048):
        for move in cube_REO_v2.moves:

            remember_eo = EO_table[x]

            #pass the corresponding edge orientation
            cube_REO_v2.w = list(EO_table[x])

            #apply the move
            cube_REO_v2.scramble_read([move])

            string_EO = list_in_str(cube_REO_v2.w)

            #deduce the index of the new edge oriention
            y = EO_table_reverse[string_EO]

            #give the rewards accordingly
            if cube_REO_v2.number_NEO(cube_REO_v2.w) == 0:
                REO_table_v2[x][y] = 100
            else:
                REO_table_v2[x][y] = 0
            
            

else:
    with open(start_REO_table_v2, "rb") as f:
        REO_table_v2 = pickle.load(f)


with open(f"3x3_tables/REO-tablev2.pickle", "wb") as f:
    pickle.dump(REO_table_v2, f)


move_step2 = ["R", "Ri", "R2", "L", "Li", "L2", "F2", "B2", "U", "Ui", "U2", "D", "Di", "D2"]

#The action space is now 14, however the state is bigger, indeed there is 3^7 possible corner orientation and 495 possible permutations for edges.
#We need to create a table where there is a possible state listed.
#We first create the table of all possible corner orientation

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

#We create a list with all possible coordinates for edges 5, 6, 7 and 8 
ME = []

#This can be first listed as all binary number of length 12 with exactly 4 ones. We can reuse EOs

intermediate_ME = []

for edge in EOs:
    if sum(edge) == 4:
        intermediate_ME.append(edge)


for edge in intermediate_ME:
    ME.append(ME_coordinates2(edge))

ME_table = {}

counter6 = 0
for edge in ME:
    ME_table[counter6] = edge
    counter6 += 1

intermediate_ME_table = {}

counter7 = 0
for edge in intermediate_ME:
    intermediate_ME_table[counter7] = edge
    counter7 += 1

str_ME = []

for edge in intermediate_ME:
    str_ME.append(list_in_str(edge))

ME_table_reverse = {}

counter8 = 0
for edge in str_ME:

    ME_table_reverse[edge] = counter8
    counter8 += 1


cube_2 = Cube(Permutation(), Permutation(), [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0])

#state tables for step2
Step2_table1 = {}

counter = 0
for co in range(729):
    for me in range(495):
        Step2_table1[counter] = (COs[co], intermediate_ME[me])

        counter += 1

Step2_table2 = {}

counter = 0
for co in range(729, 1458):
    for me in range(495):
        Step2_table2[counter] = (COs[co], intermediate_ME[me])

        counter += 1

Step2_table3 = {}

counter = 0
for co in range(1458, 2187):
    for me in range(495):
        Step2_table3[counter] = (COs[co], intermediate_ME[me])

        counter += 1



Step2_table1_reverse = {}
counter = 0
for co in range(729):
    for me in range(495):
        Step2_table1_reverse[str_CO[co] + str_ME[me]] = counter

        counter += 1


Step2_table2_reverse = {}
counter = 0
for co in range(729, 1458):
    for me in range(495):
        Step2_table2_reverse[str_CO[co] + str_ME[me]] = counter

        counter += 1

Step2_table3_reverse = {}
counter = 0
for co in range(1458, 2187):
    for me in range(495):
        Step2_table3_reverse[str_CO[co] + str_ME[me]] = counter

        counter += 1


start_R2_table1 = "3x3_tables/R2-table1.pickle"


if start_R2_table1 is None:

    R2_table_1 = np.zeros(shape= (729*495, 14))


    for x in range(729*495):
        for y in range(14):
            
            #current coordinate for CO and middle edges
            cube_2.v = Step2_table1[x][0]
            cube_2.MDE_coordinates = Step2_table1[x][1]

            #apply the move
            cube_2.scramble_read([move_step2[y]])
            
            #give the reward accordingly
            if cube_2.number_NCO() == 0 and cube_2.ME_coordinates() == [5, 6, 7, 8]:
                R2_table_1[x][y] = 100
            
            else:
                R2_table_1[x][y] = 0
else:
    with open(start_R2_table1, "rb") as f:
        R2_table_1 = pickle.load(f)

with open(f"3x3_tables/R2-table1.pickle", "wb") as f:
    pickle.dump(R2_table_1, f)



start_R2_table2 = "3x3_tables/R2-table2.pickle"


if start_R2_table2 is None:

    R2_table_2 = np.zeros(shape= (729*495, 14))


    for x in range(729*495):
        for y in range(14):

            #current coordinate for CO and middle edges
            cube_2.v = Step2_table2[x][0]
            cube_2.MDE_coordinates = Step2_table2[x][1]

            #apply the move
            cube_2.scramble_read([move_step2[y]])

            #give the reward accordingly
            if cube_2.number_NCO() == 0 and cube_2.ME_coordinates() == [5, 6, 7, 8]:
                R2_table_2[x][y] = 100
            
            else:
                R2_table_2[x][y] = 0
else:
    with open(start_R2_table2, "rb") as f:
        R2_table_2 = pickle.load(f)

with open(f"3x3_tables/R2-table2.pickle", "wb") as f:
    pickle.dump(R2_table_2, f)



start_R2_table3 = "3x3_tables/R2-table3.pickle"

if start_R2_table3 is None:

    R2_table_3 = np.zeros(shape= (729*495, 14))


    for x in range(729*495):
        for y in range(14):
            
            #current coordinate for CO and middle edges
            cube_2.v = Step2_table3[x][0]
            cube_2.MDE_coordinates = Step2_table3[x][1]
            
            #apply the move
            cube_2.scramble_read([move_step2[y]])

            #give the reward accordingly
            if cube_2.number_NCO() == 0 and cube_2.ME_coordinates() == [5, 6, 7, 8]:
                R2_table_3[x][y] = 100
            
            else:
                R2_table_3[x][y] = 0
else:
    with open(start_R2_table3, "rb") as f:
        R2_table_3 = pickle.load(f)

with open(f"3x3_tables/R2-table3.pickle", "wb") as f:
    pickle.dump(R2_table_3, f)