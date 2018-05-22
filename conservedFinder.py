import csv, math
import numpy as np
fileName = "578_Example.fasta"



def conservedFinder(array):
    np.set_printoptions(threshold=np.inf)
    from collections import defaultdict
    no_sequence, sequence = 0, ""
    #seq = input('Enter FASTA seq. file name:')

    for i in range(len(array[0])):
        temp = array[1][i]
        



    for each_seq in seq_list:
        for i in range(seq_len):
            if each_seq[i] == "A":
                mat[0][i] += 1
            elif each_seq[i] == "C":
                mat[1][i] += 1
            elif each_seq[i] == "G":
                mat[2][i] += 1
            elif each_seq[i] == "U":
                mat[3][i] += 1
            elif each_seq[i] == "-":
                mat[4][i] += 1 
    print(mat)            
