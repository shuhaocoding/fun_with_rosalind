from Bio import SeqIO
from Bio.Seq import Seq
import re

# Parse the sequencs into a list
fasta_sequences = SeqIO.parse(open("rosalind_lcsm.txt"), 'fasta')
l = []
for fasta in fasta_sequences:
    l.append(str(fasta.seq))

# Start with 4-mers
length = 4
# Generate a list that stores a set of 4-mers from each sequence
setlist = []
for seq in l:
    s = set()
    for i in range(len(seq) - 3):
        s.add(seq[i:i + 4])
    setlist.append(s)
# Based on the above list generate a set of all the 4-mers form all the sequences
s = setlist[0]
for sets in setlist:
    s = s & sets


# Define a function that updates a new set of (k+1)-mers, k starting with 4
def update_kmers(s, length):
    totalNo = 0
    d = {}
    for seq in l:
        for substring in s:
            totalNo += seq.count(substring)  # Count the occurrence of k-mers in each sequence
        d[seq] = totalNo
    seqlist = []
    for key, value in d.items():
        if value == min(d.values()):
            seqlist.append(key)  # Find a candidate sequence with the smallest number of k-mer occurrence
    candidate_seq = seqlist[0]

    # Find the positions of kmers
    poslist = []
    new_s = set()
    for substring in s:
        poslist += [m.start() for m in re.finditer(substring, candidate_seq)]
        # Update (k+1)mers
    for i in poslist:
        new_s.add(candidate_seq[i:i + length + 1])
    length += 1

    # Check if the (k+1)mer is a common substring
    for substring in list(new_s):
        if len(substring) != length:
            new_s.remove(substring)
        for seq in l:
            if substring not in seq:
                new_s.remove(substring)
                break
    if len(new_s) > 0:
        return new_s, length
    return 'done'


# Execute the above function until there is no available (k+1)mer substring
while True:
    if update_kmers(s, length) == 'done':
        break
    s, length = update_kmers(s, length)
print(s)
