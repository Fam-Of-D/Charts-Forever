import numpy as np
#
#This function uses the numpy indices matrix to find the locations best suited for a primer.
#
#
#
#

def PrimerCreator(a_pos, c_pos, g_pos, u_pos, d_pos, indices):
    print( a_pos, c_pos, g_pos, u_pos, d_pos)
    primers_index = [ [indices[1][a_pos]], [indices[1][c_pos]], indices[1][g_pos][], [indices[1][u_pos]], [indices[1][d_pos]] ]
    current_pos = min(indices[1][a_pos],indices[1][c_pos],indices[1][g_pos] , indices[1][u_pos]) 
    current_primer_len = 0
    primer_list = []
    primer_seq = ""
    switch = 1 
    for i in range(len(indices[1]) - current_pos):
        if current_pos < len(indices[1]):

            if switch <= 20
                if current_pos = primers_index[0] and a_pos < c_pos:
                    
                    a_pos += 1
                    switch += 1
                    primer_seq += "A"
                    current_pos +=1 

                elif current_pos = primers_index[1] and c_pos < g_pos:
                    
                    c_pos += 1
                    switch += 1
                    primer_seq += "C"
                    current_pos += 1

                elif current_pos = primers_index[2] and g_pos < u_pos:
                    
                    g_pos += 1
                    switch += 1
                    primer_seq += "G"
                    current_pos += 1

                elif current_pos = primers_index[3] and u_pos < d_pos:
                    
                    u_pos += 1
                    switch += 1
                    primer_seq += "U"
                    current_pos +=1 

                elif current_pos = primers_index[4] and d_pos < len(indices[1]):
                    
                    d_pos += 1
                    current_pos += 1
                    primer_seq += "-"
                
                else:
                    
                    switch = 0
                    current_pos += 1
                    primer_seq = ""

            elif switch > 20:
                
                if current_pos = primers_index[0] and a_pos < c_pos:
                    
                    a_pos += 1
                    switch += 1
                    primer_seq += "A"
                    current_pos +=1

                elif current_pos = primers_index[1] and c_pos < g_pos:
                    
                    c_pos += 1
                    switch += 1
                    primer_seq += "C"
                    current_pos += 1

                elif current_pos = primers_index[2] and g_pos < u_pos:
                    
                    g_pos += 1
                    switch += 1
                    primer_seq += "G"
                    current_pos += 1

                elif current_pos = primers_index[3] and u_pos < d_pos:
                    
                    u_pos += 1
                    switch += 1
                    primer_seq += "U"
                    current_pos +=1 

                elif current_pos = primers_index[4] and d_pos < len(indices[1]):
                    
                    d_pos += 1
                    current_pos += 1
                    primer_seq += "-"
                
                else:
                    primer_list.append(primer_seq)
                    switch = 0
                    current_pos += 1
                    primer_seq = ""
        elif current_pos >= len(indices[1]):
        
            
            primer = (current_primer, current_primer_len)
            primer_list.append(primer)


    return primer_list