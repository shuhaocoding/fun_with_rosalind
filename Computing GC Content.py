from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import GC
import os

# Set the working directory and download the fasta file
os.chdir("/Users/shuhao/Desktop")
# Parse the fasta sequences
fasta_sequences = SeqIO.parse(open("rosalind_gc.txt"),'fasta')
# Generate a dictionary containing sequence GC content as keys, and sequence ID as values.
GC_dic = {}
for fasta in fasta_sequences:
    GC_dic[GC(Seq(str(fasta.seq)))] = fasta.id
GC_max = max(GC_dic.keys())
print(GC_dic[GC_max])
print(GC_max)

