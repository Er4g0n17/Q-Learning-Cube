import numpy as np
from sympy.combinatorics import Permutation
from sympy.interactive import init_printing
from sympy.combinatorics.polyhedron import Polyhedron
from sympy.combinatorics.perm_groups import PermutationGroup


class Cube:
    """p is the current permutation of corners, e is the current permutation of edges, v is the current orientation of corners 
        and w is the current permutation of edges."""
    def __init__(self, p, e, v, w, MDE_coordinates):
        self.p = p #Permutation corners
        self.e = e #Permutation edges
        self.v = v #Orientation corners
        self.w = w #Orientation edges
        self.MDE_coordinates = MDE_coordinates #Four middle edges, length 12 list where 1 are the E-slice edges and 0 others.
    
    #moves for step 1
    moves = ["R", "Ri", "R2", "L", "Li", "L2", "F", "Fi", "F2", "B", "Bi", "B2", "U", "Ui", "U2", "D", "Di", "D2"]
    
    #moves for step 2
    moves2 = ["R", "Ri", "R2", "L", "Li", "L2", "F2", "B2", "U", "Ui", "U2", "D", "Di", "D2"]

    #Righ movement
    def R(self):

        p_R = Permutation(2, 6, 7, 3) #Permutation on Corners
        e_R = Permutation(2, 6, 10, 7) #Permutation 
        
        v_R = [0, 1, 2, 0, 0, 2, 1, 0]
        w_R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.p = self.p * p_R
        self.e = self.e * e_R

        e_R_full = Permutation(e_R, size = 13)
        self.MDE_coordinates = [self.MDE_coordinates[(i^(e_R_full**-1))-1] for i in range(1,13)]

    #We modify the array of edge orientation
        counter_e = 0
        for eo in self.w:
            if counter_e == 1:
                #it will go to 5
                remember_e1 = eo
            elif counter_e == 5:
                #assigne the new value and remember this one.
                self.w[counter_e] = remember_e1
                remember_e1 = eo
            elif counter_e == 6: 
                remember_e2 = eo
            elif counter_e == 9: 
                self.w[counter_e] = remember_e1
                remember_e1 = eo
                self.w[6] = remember_e1
                self.w[1] = remember_e2
            counter_e += 1

    #We modify the array of corner orientation
    #We try a different method for corners

        p_R_full = Permutation(p_R, size = 9)
        #we change the place of the corner, we then use the corner orientation list v_R to add it to the old
        #one and use mod 3 to ensure it respects the requirements.
        self.v = [(self.v[(i^(p_R_full**-1))-1]+v_R[i-1])%3 for i in range(1,9)]
        """ counter_c = 0
        for co in self.v:
        if counter_c == 1:
                remember_c1 = co
            elif counter_c == 5:
                self.w[counter_c] = (remember_c1 + 1)%3
                remember_c1 = co
        """
        #print("applied R to cube")
   
    def L(self):
        p_L = Permutation(1, 4, 8, 5) #Permutation on Corners
        e_L = Permutation(4, 8, 12, 5) #Permutation 

        v_L = [2, 0, 0, 1, 1, 0, 0, 2]
        w_L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.p = self.p * p_L
        self.e = self.e * e_L

        e_L_full = Permutation(e_L, size = 13)
        self.MDE_coordinates = [self.MDE_coordinates[(i^(e_L_full**-1))-1] for i in range(1,13)]

        counter_e = 0
        for eo in self.w:
            if counter_e == 3:
                remember_e1 = eo
            elif counter_e == 4:
                remember_e2 = eo
            elif counter_e == 7:
                self.w[counter_e] = remember_e1
                remember_e1 = eo
            elif counter_e == 11: 
                self.w[counter_e] = remember_e1
                remember_e1 = eo
                self.w[4] = remember_e1
                self.w[3] = remember_e2
            counter_e += 1
        

        #We update corner orientation
        p_L_full = Permutation(p_L, size = 9)

        self.v = [(self.v[(i^(p_L_full**-1))-1]+v_L[i-1])%3 for i in range(1,9)]



    def U(self):
        p_U = Permutation(1, 2, 3, 4) #Permutation on Corners
        e_U = Permutation(1, 2, 3, 4) #Permutation 

        v_U = [0, 0, 0, 0, 0, 0, 0, 0]
        w_U = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.p = self.p * p_U
        self.e = self.e * e_U

        e_U_full = Permutation(e_U, size = 13)
        self.MDE_coordinates = [self.MDE_coordinates[(i^(e_U_full**-1))-1] for i in range(1,13)]

        counter_e = 0
        for eo in self.w:
            if counter_e == 0:
                remember_e1 = eo
            elif counter_e == 1:
                self.w[counter_e] = remember_e1
                remember_e1 = eo
            elif counter_e == 2:
                self.w[counter_e] = remember_e1 
                remember_e1 = eo
            elif counter_e == 3: 
                self.w[counter_e] = remember_e1
                remember_e1 = eo
                self.w[0] = remember_e1
            counter_e += 1
        
        #print("applied U to cube")

        #We update corner permutation
        #Use same method as for edges
        counter_c = 0

        for co in self.v:
            if counter_c == 0:
                remember_c1 = co
            elif counter_c == 1:
                self.v[counter_c] = remember_c1
                remember_c1 = co
            elif counter_c == 2:
                self.v[counter_c] = remember_c1
                remember_c1 = co
            elif counter_c == 3:
                self.v[counter_c] = remember_c1
                remember_c1 = co
                self.v[0] = remember_c1
            counter_c += 1

    def D(self):
        p_D = Permutation(5, 8, 7, 6) #Permutation on Corners
        e_D = Permutation(9, 12, 11, 10) #Permutation 

        v_D = [0, 0, 0, 0, 0, 0, 0, 0]
        w_D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.p = self.p * p_D
        self.e = self.e * e_D

        e_D_full = Permutation(e_D, size = 13)
        self.MDE_coordinates = [self.MDE_coordinates[(i^(e_D_full**-1))-1] for i in range(1,13)]

        counter_e = 0
        for eo in self.w:
            if counter_e == 8:
                remember_e1 = eo
            elif counter_e == 9:
                remember_e2 = eo
            elif counter_e == 10:
                remember_e3 = eo
            elif counter_e == 11: 
                self.w[counter_e] = remember_e1
                remember_e1 = eo
                self.w[10] = remember_e1
                self.w[9] = remember_e3
                self.w[8] = remember_e2

            counter_e += 1
        
        counter_c = 0
        for co in self.v:
            if counter_c == 4:
                remember_c1 = co
            elif counter_c == 5:
                remember_c2 = co
            elif counter_c == 6:
                remember_c3 = co
            elif counter_c == 7:
                self.v[counter_c] = remember_c1
                remember_c1 = co
                self.v[6] = remember_c1
                self.v[5] = remember_c3
                self.v[4] = remember_c2
            counter_c += 1
        
        #print("applied D to cube")

    def B(self):
        p_B = Permutation(1, 5, 6, 2) #Permutation on Corners
        e_B = Permutation(1, 5, 9, 6) #Permutation 

        v_B = [1, 2, 0, 0, 2, 1, 0, 0] 
        w_B = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0]

        self.p = self.p * p_B
        self.e = self.e * e_B

        e_B_full = Permutation(e_B, size = 13)
        self.MDE_coordinates = [self.MDE_coordinates[(i^(e_B_full**-1))-1] for i in range(1,13)]
   
        counter_e = 0
        for eo in self.w:
            if counter_e == 0:
                remember_e1 = eo
            elif counter_e == 4:
                self.w[counter_e] = (remember_e1 + 1) % 2
                remember_e1 = eo
            elif counter_e == 5:
                remember_e2 = eo
            elif counter_e == 8: 
                self.w[counter_e] = (remember_e1 + 1) % 2
                remember_e1 = eo
                self.w[5] = (remember_e1 + 1) % 2
                self.w[0] = (remember_e2 + 1) % 2

            counter_e += 1

        #update corner orientation
            
        p_B_full = Permutation(p_B, size = 9)

        self.v = [(self.v[(i^(p_B_full**-1))-1]+v_B[i-1])%3 for i in range(1,9)]
        #print("applied B to cube")


    def F(self):
        p_F = Permutation(3, 7, 8, 4) #Permutation on Corners
        e_F = Permutation(3, 7, 11, 8) #Permutation 

        v_F = [0, 0, 1, 2, 0, 0, 2, 1]
        w_F = [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0]

        self.p = self.p * p_F
        self.e = self.e * e_F

        e_F_full = Permutation(e_F, size = 13)
        self.MDE_coordinates = [self.MDE_coordinates[(i^(e_F_full**-1))-1] for i in range(1,13)]

        counter_e = 0

        for eo in self.w:
            if counter_e == 2:
                remember_e1 = eo
            elif counter_e == 6:
                self.w[counter_e] = (remember_e1 + 1) % 2
                remember_e1 = eo
            elif counter_e == 7:
                remember_e2 = eo
            elif counter_e == 10: 
                self.w[counter_e] = (remember_e1 + 1) % 2
                remember_e1 = eo
                self.w[7] = (remember_e1 + 1) % 2
                self.w[2] = (remember_e2 + 1) % 2

            counter_e += 1
            
        #update corner orientation
        p_F_full = Permutation(p_F, size = 9)

        self.v = [(self.v[(i^(p_F_full**-1))-1]+v_F[i-1])%3 for i in range(1,9)]
        

        #print("applied F to cube")

    #To simplify, we will now define inverses and double moves as combinations of the six base moves
    #We can implement them properly later.
    def R_i(self):
        self.R()
        self.R()
        self.R()
        
    def R2(self):
        self.R()
        self.R()

    def L_i(self):
        self.L()
        self.L()
        self.L()
    
    def L2(self):
        self.L()
        self.L()

    def F_i(self):
        self.F()
        self.F()
        self.F()
    
    def F2(self):
        self.F()
        self.F()

    def B_i(self):
        self.B()
        self.B()
        self.B()
    
    def B2(self):
        self.B()
        self.B()

    def U_i(self):
        self.U()
        self.U()
        self.U()
    
    def U2(self):
        self.U()
        self.U()
    
    def D_i(self):
        self.D()
        self.D()
        self.D()
    
    def D2(self):
        self.D()
        self.D()

    def scramble_read(self, scramble):
        
    #move_dic = {"R": self.R(), "R'": self.R_i(), "R2": self.R2(), "L": self.R(), "L'": self.L_i(), "R2": self.L2(), "F": self.F(), "F'": self.F_i(), "F2": self.F2(), "B": self.B(), "B'": self.B_i(), "B2": self.B2(), "U": self.U(), "U'": self.U_i(), "U2": self.U2(), "D": self.D(), "D'": self.D_i(), "D2": self.D2()}

        
        for move in scramble:
            

            if move == "R":
                self.R()
            elif move == "Ri":
                self.R_i()
            elif move == "R2":
                self.R2()
            elif move == "L":
                self.L()
            elif move == "Li":
                self.L_i()
            elif move == "L2":
                self.L2()
            elif move == "U":
                self.U()
            elif move == "Ui":
                self.U_i()
            elif move == "U2":
                self.U2()
            elif move == "D":
                self.D()
            elif move == "Di":
                self.D_i()
            elif move == "D2":
                self.D2()
            elif move == "F":
                self.F()
            elif move == "Fi":
                self.F_i()
            elif move == "F2":
                self.F2()
            elif move == "B":
                self.B()
            elif move == "Bi":
                self.B_i()
            elif move == "B2":
                self.B2()

        #print("applied: " + sbl + "to cube")

    #return the number of bad edges
    def number_NEO(self, w):
        return sum(w)
        """ n_neo = 0
        for neo in w:
            if neo == 1:
                n_neo += 1
        
        return n_neo
        """
    
    #return the number of bad corners
    def number_NCO(self):
        n_nco = 0
        for co in self.v:
            if co != 0:
                n_nco += 1
        
        return n_nco
    
    #return coordinates of middle layer edges
    def ME_coordinates(self):
        coordinate = []
        counter = 1
        for edge in self.MDE_coordinates:
            if edge != 0:
                coordinate.append(counter)
            
            counter += 1
        return coordinate

    #take coordinates and transform it to length 12 list form
    def ME_coordinates_reverse(coordinate):
        me = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for x in coordinate:
            me[x] = 1
        
        return me

    def number_ME_in_E(self):

        index = 0
        number = 0
        for edge in self.MDE_coordinates:
            if index == 4 or index == 5 or index == 6 or index == 7:
                if edge != 0:
                    number += 1

            index += 1
        
        return number

    def ME_2_edges(self):
        half_edges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        index = 0

        for edge in self.MDE_coordinates:
            if edge == 5 or edge == 8:
                half_edges[index] = 1
            else:
                half_edges[index] = 0
            
            index += 1
        
        return half_edges


        
        
            
#Let's create a table with all possible eo
#for edge in range(11):
    #for orientation in range(1):
      #  if edge < 10:
        #    EO[edge] = orientation
      #  elif edge == 10:
       #     EO[edge] = orientation
        #    EO[edge + 1] = orientation
 

def number_NEO2(w):
        return sum(w)


def number_NCO2(v):
    n_nco = 0
    for co in v:
        if co != 0:
            n_nco += 1
    
    return n_nco

def ME_coordinates2(coordinates):
    coordinate = []
    counter = 1
    for edge in coordinates:
        if edge != 0:
            coordinate.append(counter)
        
        counter += 1
    return coordinate

def ME_coordinates_reverse(coordinate):
    me = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for x in coordinate:
        me[x-1] = 1
    
    return me

def number_ME_in_E2(coordinate):

    index = 0
    number = 0
    for edge in coordinate:
        if index == 4 or index == 5 or index == 6 or index == 7:
            if edge != 0:
                number += 1

        index += 1
    
    return number



def list_in_str(lists):
    string = ""
    for elem in lists:
        string = string + str(elem)

    return string


#translate the list form in str form using a dic and by iterating through the list
def scramble_translator(scramble):
    new = ""

    move_dic = {"R": "R", "Ri": "R'", "R2": "R2", "L": "L", "Li": "L'", "L2": "L2", "F": "F", "Fi": "F'", "F2": "F2", "B": "B", "Bi": "B'", "B2": "B2", "U": "U", "Ui": "U'", "U2": "U2", "D": "D", "Di": "D'", "D2": "D2"}

    for move in scramble:

        new += move_dic[move]

    return new

def str_scramble_to_list_scramble(scramble):

    new = []
    move_dic = {"R": "R", "R'": "Ri", "R2": "R2", "L": "L", "L'": "Li", "L2": "L2", "F": "F", "F'": "Fi", "F2": "F2", "B": "B", "B'": "Bi", "B2": "B2", "U": "U", "U'": "Ui", "U2": "U2", "D": "D", "D'": "Di", "D2": "D2"}

    list_scramble = scramble.split(" ")

    for move in list_scramble:
        new.append(move_dic[move])

    return new

