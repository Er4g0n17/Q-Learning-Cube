from QLearningCO2x2 import *
from QLearningCP2x2 import *
from Cube2x2 import *
import webbrowser


scramble = input("Scramble?",)

scramble_translated = str_scramble_to_list_scramble(scramble)

webbrowser.open("https://alg.cubing.net/?setup=" + scramble +"&puzzle=2x2x2", new=0)


co_solution = qCO2x2(scramble_translated)

scramble_CO = scramble_translated + co_solution

cp_solution = qCP2x2(scramble_CO)

final_solution = co_solution + cp_solution



solution = scramble_translator(final_solution)

webbrowser.open("https://alg.cubing.net/?setup=" + scramble + "&alg=" + solution + "&puzzle=2x2x2", new=0)

print("Solution for scramble", scramble, "is:")
print(final_solution)