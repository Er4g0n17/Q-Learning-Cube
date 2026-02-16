# QLearning-Cube

Cube.py is the Rubik's cube implementation. Only permutations and edge orientations are supported for now. Some librairies are needed to be installed to use the program.
Cube2x2.py is the 2x2 Rubik's cube implementation.

Rtable.py creates the q-table with the corresponding reward for each state and action. Need to put tables as None to create them.
Rtable2x2.py creates the reward tables for the corner orientation step and the final step where we solve the permutation.


Qtable-Step2.py creates the q-tables for Step 2.
QtableCO2x2.py and QtableCP2x2.py apply respectively the Q-learning algorithm on the Corner Orientation and on the Corner Permutation using the reward tables to create Q-tables.

QLearningCO2x2.py and QLearningCP2x2.py use the Q-tables to find a solution for the Corner Orientation and the Corner Permutation.

Scrambe_Functions_Step1and2_2x2.py contains functions that are used to find solutions.

2x2Solver.py takes a scramble on a 2x2 cube, gives back the solution and shows it the website alg.cubing.net using the solutions found from QLearningCO2x2.py and QLearningCP2x2.py.
