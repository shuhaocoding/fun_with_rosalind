import numpy as np
from Bio import SeqIO

# Parse the input sequences into a list
fasta_sequences = SeqIO.parse(open("rosalind_cons.txt"),'fasta')
l = []
for fasta in fasta_sequences:
    l.append(str(fasta.seq))

# Generate the profile matrix, starting with zeros    
P = np.zeros((4, len(l[0])))
# Map the base counts to a row index in the matrix
map_dic = {'A':0, 'C':1, 'G':2, 'T':3}
# Count the occurrence of each bases and output to the matrix
for seq in l:
    for pos, base in enumerate(seq):
        P[map_dic[base], pos] += 1
# Print the matrix in the requested format 
letters='ACGT'
for row, counts in enumerate(P):
    count_list=list(counts)
    count_char=map(str, map(int, count_list))
    count_string=' '.join(count_char)
    print(letters[row]+': '+count_string)

# Reverse map the row index to base counts
map_dic2 = {0:'A', 1:'C', 2:'G', 3:'T'}
# Generate the consensus string by finding the most frequent base
C = ''
index = list(np.argmax(P, axis=0))
for i in index:
    C += map_dic2[i]
print(C)


