fastaFile = "40k_Example.fasta"

def SequencePackager(Taxonomy, level):
#This is going to find the taxonomies conservedness for the 16s rRna 
    
    

    file = open(fastaFile ,'r')

    sequence = ""
    no_sequences = 0
    packet_counter = 0
    fileName = Taxonomy + ".fasta"
    counter = 0

    for line in file:
        if ">" in line:
            
            if counter: 
                if packet_counter <= no_sequences:
                    if packet_counter == 1:
                        packet_file = open(fileName, "w+")
                        packet_file.write(sequence)
                    else:
                        packet_file = open(fileName, "a")
                        packet_file.write(sequence)
                        print(packet_counter)
            counter = 0


            meta = line
            meta_list = meta.split(";")

            if meta_list[level] == Taxonomy:
                sequence = line
                counter = 1
                packet_counter += 1 

        else:
            sequence = sequence + line

    return fileName