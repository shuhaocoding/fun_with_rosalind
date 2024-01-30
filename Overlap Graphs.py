from Bio import SeqIO
from Bio.Seq import Seq

# Parse the sequences
fasta_sequences = SeqIO.parse(open("rosalind_grph.txt"),'fasta')
reverse_fa = {} # Generate a dic that contains sequences as keys and IDs as values
for record in fasta_sequences:
    reverse_fa[str(record.seq)] = record.id

# Define a function that outputs directed edges
def endOverlap(a, b):
    if b.startswith(a[-3:]):
        print(reverse_fa[a] + ' ' + reverse_fa[b])

# Perform the above function for every sequence pairs in the input file
for query in reverse_fa.keys():
    testlist = list(reverse_fa.keys())
    testlist.remove(query)
    for seq in testlist:
        endOverlap(query, seq)

