from Bio import SeqIO
from Bio.Seq import Seq

fasta_sequences = SeqIO.parse(open("rosalind_grph.txt"),'fasta')
d = {}
for fasta in fasta_sequences:
    d[str(fasta.seq)] = fasta.id


def endOverlap(a, b):
    if b.startswith(a[-3:]):
        print(d[a] + ' ' + d[b])

for query in d.keys():
    testlist = list(d.keys())
    testlist.remove(query)
    for seq in testlist:
        endOverlap(query, seq)

