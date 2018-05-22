import csv, math
import numpy as np
threshold = 0.70

def packet_Analyzer(fileName):
    
    np.set_printoptions(threshold=np.inf)
    from collections import defaultdict
    no_sequence, sequence = 0, ""
    #seq = input('Enter FASTA seq. file name:')

    with open(fileName) as f:
        for line in f:
            if line[0] == ">":
                no_sequence += 1
                if no_sequence > 1:
                    break
            else:
                sequence += line.replace(" ", "").strip()

    seq_len = len(sequence)
    mat = np.zeros((5, len(sequence)), dtype=int)
    no_sequence = 0

    seq_list = []
    with open(fileName) as f:
        for line in f:
            if line[0] == ">":
                no_sequence += 1    
                if no_sequence > 1:
                    seq_list.append(sequence)      
                sequence = ""
            else:
                sequence += line.replace(" ", "").strip()
    seq_list.append(sequence)

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
    #print(mat)            

    cons_limit = int((threshold)*no_sequence)

    #for i in range(seq_len):
    #   if mat[0][i] > cons_limit:

    indexes = np.where(mat > cons_limit)

    return indexes
    