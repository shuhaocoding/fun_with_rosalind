from Bio import SeqIO
from Bio.Seq import Seq

# Parse the sequences
for fasta in SeqIO.parse(open("rosalind_revp.txt"),'fasta'):
    seq = str(fasta.seq)

# Find all the reverse palindromes
for i in range(4,13):
    for count, letter in enumerate(seq[:len(seq)-i+1]):
        if str(Seq(seq[count:count+i]).reverse_complement()) == seq[count:count+i]:
            print(count+1, i)
