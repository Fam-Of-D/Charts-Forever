import numpy as np


def percentageCalculator(fastaFile, uniqueList):
    file = open(fastaFile, "r")
    kingdoms = np.zeros(len(uniqueList[0]))
    phylums = np.zeros(len(uniqueList[1]))
    classes = np.zeros(len(uniqueList[2]))
    orders = np.zeros(len(uniqueList[3]))

    for line in file:
        
        if '>' == line[0]:
            Taxonomy = line.split(";")
            Taxonomy.pop(0)

            for i in range(len(kingdoms)):
                if uniqueList[0][i] == Taxonomy[0]:
                    kingdoms[i] += 1

            for i in range(len(phylums)):  
                if uniqueList[1][i] == Taxonomy[1]:
                    phylums[i] += 1

            for i in range(len(classes)): 
                if uniqueList[2][i] == Taxonomy[2]:
                    classes[i] += 1


    print(kingdoms, phylums, classes)
                    
            