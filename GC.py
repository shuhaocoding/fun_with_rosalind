from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import GC

fasta_sequences = SeqIO.parse(open("rosalind_gc.txt"),'fasta')
d = {}
for fasta in fasta_sequences:
    d[GC(Seq(str(fasta.seq)))] = fasta.id
GC_max = max(d.keys())
print(d[GC_max])
print(GC_max)

