import numpy as np
from Bio import SeqIO

fasta_sequences = SeqIO.parse(open("rosalind_cons.txt"),'fasta')
l = []
for fasta in fasta_sequences:
    l.append(str(fasta.seq))
    
P = np.zeros((4, len(l[0])))
d = {'A':0, 'C':1, 'G':2, 'T':3}
for seq in l:
    for pos,letter in enumerate(seq):
        P[d[letter],pos]+=1

d2 = {0:'A', 1:'C', 2:'G', 3:'T'}
c = ''
index = list(np.argmax(P, axis=0))
for i in index:
    c+=d2[i]

print(c)
letters='ACGT'
for i_number, i in enumerate(P):
    new_i=list(i)
    string_list=map(str, map(int, new_i))
    the_string=' '.join(string_list)
    print(letters[i_number]+': '+the_string)
