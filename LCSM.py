from Bio import SeqIO
from Bio.Seq import Seq
import re

fasta_sequences = SeqIO.parse(open("rosalind_lcsm.txt"),'fasta')
l = []
for fasta in fasta_sequences:
    l.append(str(fasta.seq))
    
# start with 4-mers
length = 4
l2 = []
for seq in l:
    s = set()
    for i in range(len(seq)-3):
        s.add(seq[i:i+4])
    l2.append(s)
s = l2[0]
for sets in l2:
    s = s&sets
    
def update_kmers(s, length):
    # find candidate sequence
    totalNo = 0
    d = {}
    for seq in l:
        for substring in s:
            totalNo += seq.count(substring)
        d[seq] = totalNo
    seqlist = []
    for key, value in d.items():
             if value == min(d.values()):
                 seqlist.append(key)
    candidate_seq = seqlist[0]

    #find position for each kmer
    poslist = []
    for substring in s:
        poslist += [m.start() for m in re.finditer(substring, candidate_seq)]

    # find k+1mer    
    s2 = set()
    for i in poslist:
        s2.add(candidate_seq[i:i+length+1])
    length += 1

    #check if it is a common substring
    for substring in list(s2):
        if len(substring) != length:
            s2.remove(substring)
        for seq in l:
            if substring not in seq:
                s2.remove(substring)
                break
    if len(s2) > 0:
        return s2, length
    return 'done'

while True:
    if update_kmers(s, length) == 'done':
        break
    s, length = update_kmers(s, length)
    print(len(s),s)


    
    
    
    
    
    
    
    
    
    
    
