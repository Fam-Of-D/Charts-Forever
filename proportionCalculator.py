
fastaFile = "nonRedundantBacteriaSilva."

def proportionCalculator(Taxonomies,fastaFile):
    """ Input is the taxonomy level wanted...""" 

    levelOne = [0] * len(Taxonomies[1])
    levelTwo = [0] * len(Taxonomies[2])
    levelThree = [0] * len(Taxonomies[3])
    levelFour = [0] * len(Taxonomies[4])

    count_Taxa = [levelOne, levelTwo, levelThree, levelFour]
    file = open(fastaFile ,'r')
    for line in file:
        
        if '>' == line[0]:
            #This stores the taxonomy
            meta = line
            meta_list = meta.split(";")
            #if len(meta_list) < 5:
            #    break
            print(meta)
            print(meta_list)
            print(meta_list[1])
            print(Taxonomies[1][0])
            for i in range(1, len(Taxonomies)):
                for j in range(len(Taxonomies[i])):
                    print(Taxonomies[i][j])
                    if len(meta_list) < i + 1 :
                        continue
                    if meta_list[i] == Taxonomies[i][j]:
                        print(meta_list[i], Taxonomies[i][j], i, j)
                        count_Taxa[i-1][j] += 1
    file.close()
    print(Taxonomies)
    return count_Taxa


def uniqueTaxonomy(fileName):
    """ Input is the taxonomy level wanted.
    """ 
    Taxonomy = []
    Kingdoms = []
    Phylums = []
    Classes = []
    Orders = []
    Families = []
    Species = []
    uniqueList = [Kingdoms, Phylums, Classes, Orders, Families, Species]
    
    file = open(fileName ,'r')
    for line in file:

        if '>' in line[0]:
            
            Taxonomy = line.split(";")
            Taxonomy.pop(0)

            for i in range(3):
                print(len(Taxonomy)
                if Taxonomy[i] not in uniqueList[i]:
                    uniqueList[i].append(Taxonomy[i]) 
    
    file.close()

    return uniqueList


