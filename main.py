import largeFileReader2 as reader
import taxonomyEnum
import proportionCalculator
import packet_Analyzer
import conservedSites
import numpy as np
import math, csv
import PrimerCreator


fileName = "nonRedundantBacteriaSilva.fasta"
#reader.largeFileReader()  
 

#Taxonomies = taxonomyEnum.TaxonomyEnumerator()
#print(Taxonomies)
#print(proportionCalculator.proportionCalculator(Taxonomies))


indices = packet_Analyzer.packet_Analyzer(fileName)
nucleotide_pos = conservedSites.conservedSites(indices)

#print(indices) 

print ( nucleotide_pos )
primers = PrimerCreator.PrimerCreator(nucleotide_pos[0], nucleotide_pos[1],nucleotide_pos[2],nucleotide_pos[3],nucleotide_pos[4], indices)
print(primers)
#conservedSiteList = conservedSites.conservedSites(indices)

#print(conservedSiteList)