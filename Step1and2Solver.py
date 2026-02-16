import webbrowser
from time import sleep
from Cube import *

from QLearningEO3 import *
from QLearningStep2 import *


scramble = input("What is the scramble:",)

#translate the scramble from string form to list form
scramble_translated = str_scramble_to_list_scramble(scramble)

#take the eo_solution
eo_solution = EO3_solver(scramble_translated)

#translate it from str form to list form
eo_solution_translated = scramble_translator(eo_solution)

step2_solution = step2_solver(scramble_translated + eo_solution)

step2_solution_translated = scramble_translator(step2_solution)


webbrowser.open("https://alg.cubing.net/?setup=" + scramble, new=0)
sleep(1)
moves = ""

webbrowser.open("https://alg.cubing.net/?setup=" + scramble + "&alg=" + eo_solution_translated, new=0)


webbrowser.open("https://alg.cubing.net/?setup=" + scramble + eo_solution_translated + "&alg=" + step2_solution_translated, new=0)


webbrowser.open("https://alg.cubing.net/?setup=" + scramble + "&alg=" + eo_solution_translated + step2_solution_translated, new=0)

