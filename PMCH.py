import math
from Bio import SeqIO
for record in SeqIO.parse("rosalind_pmch.txt", "fasta"):
    s = str(record.seq)
# considering n pairs of A and U there will be n! perfect matchings of basepair edges
print(math.factorial(s.count('A')) * math.factorial(s.count('C')))
