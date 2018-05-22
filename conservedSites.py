import numpy as np
import csv, math


#This function gets the indices array 2x len(sequence) from the packet_Analyzer function.
# 
# The purpose of this function is to provide the sites that exceed 20chars of either A,G,C,U.
#   while counting the conserved dashed present between these chars.
# 
# This function 
# 
# This ensures that the primer made will specifically bind to this class of bacteria. 
# 
# The output of this function are the indices of >20 len chars with internal, conserved dashed of any length.
# 
#  

def conservedSites(indexes):
    C_posit = 0
    G_posit = 0
    U_posit = 0
    D_posit = 0
    A_posit = 0

    print(indexes[0])
    for i in range (len(indexes[0])-2):
        if indexes[0][i+1] != indexes[0][i]:
            switch = i + 1 
            print ("Switch " , indexes[0][i] , " to " , indexes[0][i+1] , " at index " , switch)
            if indexes[0][i+1] == 1: 
                C_posit = i + 1 
            if indexes[0][i+1] == 2: 
                G_posit = i + 1
            if indexes[0][i+1] == 3: 
                U_posit = i + 1
            if indexes[0][i+1] == 4:
                D_posit = i + 1
            
            #By the rules of packet_Analyzer.py    
    PosList = [A_posit, C_posit, G_posit, U_posit, D_posit]
    return PosList
