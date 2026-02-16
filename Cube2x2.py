import numpy as np
from sympy.combinatorics import Permutation
from sympy.interactive import init_printing
from sympy.combinatorics.polyhedron import Polyhedron
from sympy.combinatorics.perm_groups import PermutationGroup


class Cube2x2:
    """p is the current permutation of corners, v is the current orientation of corners and w is the current permutation of edges."""
    def __init__(self, p, v, cp):
        self.p = p #Permutation corners
        self.v = v #Orientation corners
        self.cp = cp
    
    #moves for step 1
    moves = ["R", "Ri", "R2", "L", "Li", "L2", "F", "Fi", "F2", "B", "Bi", "B2", "U", "Ui", "U2", "D", "Di", "D2"]
    
    #moves for step 2
    moves2 = ["R2", "L2", "F2", "B2", "U", "Ui", "U2", "D", "Di", "D2"]

    #Righ movement
    def R(self):

        p_R = Permutation(2, 6, 7, 3) #Permutation on Corners
        
        v_R = [0, 1, 2, 0, 0, 2, 1, 0]

        self.p = self.p * p_R
        
        p_R_full = Permutation(p_R, size = 9)
        self.cp = [self.cp[(i^(p_R_full**-1))-1] for i in range(1,9)]

    #We modify the array of corner orientation
    #We try a different method for corners


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
        

        v_L = [2, 0, 0, 1, 1, 0, 0, 2]

        self.p = self.p * p_L
        

        #We update corner orientation
        p_L_full = Permutation(p_L, size = 9)

        self.cp = [self.cp[(i^(p_L_full**-1))-1] for i in range(1,9)]

        self.v = [(self.v[(i^(p_L_full**-1))-1]+v_L[i-1])%3 for i in range(1,9)]



    def U(self):
        p_U = Permutation(1, 2, 3, 4) #Permutation on Corners
        
        v_U = [0, 0, 0, 0, 0, 0, 0, 0]

        self.p = self.p * p_U

        p_U_full = Permutation(p_U, size = 9)
        self.cp = [self.cp[(i^(p_U_full**-1))-1] for i in range(1,9)]
        
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

        v_D = [0, 0, 0, 0, 0, 0, 0, 0]       

        self.p = self.p * p_D

        p_D_full = Permutation(p_D, size = 9)
        self.cp = [self.cp[(i^(p_D_full**-1))-1] for i in range(1,9)]

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

        v_B = [1, 2, 0, 0, 2, 1, 0, 0] 

        self.p = self.p * p_B

        p_B_full = Permutation(p_B, size = 9)
        self.cp = [self.cp[(i^(p_B_full**-1))-1] for i in range(1,9)]
        #update corner orientation
            
        p_B_full = Permutation(p_B, size = 9)

        self.v = [(self.v[(i^(p_B_full**-1))-1]+v_B[i-1])%3 for i in range(1,9)]
        #print("applied B to cube")


    def F(self):
        p_F = Permutation(3, 7, 8, 4) #Permutation on Corners

        v_F = [0, 0, 1, 2, 0, 0, 2, 1] 

        self.p = self.p * p_F

        p_F_full = Permutation(p_F, size = 9)
        self.cp = [self.cp[(i^(p_F_full**-1))-1] for i in range(1,9)]
            
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

        sbl = ""
        
        for move in scramble:
            
            sbl += move + " "

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

    
    #return the number of bad corners
    def number_NCO(self):
        n_nco = 0
        for co in self.v:
            if co != 0:
                n_nco += 1
        
        return n_nco

#transform elements of list in a string
def list_in_str(lists):
    string = ""
    for elem in lists:
        string = string + str(elem)

    return string




