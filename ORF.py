from Bio import SeqIO
from Bio.Seq import Seq

seqrecords = list(SeqIO.parse(open("rosalind_orf.txt"), 'fasta'))
seq = str(seqrecords[0].seq)
comp_seq = str(Seq(seq).reverse_complement())

start = ["ATG"]
stop = ["TAA","TAG","TGA"]

aa_set = set()
def find_orf(seq):
    for i,letter in enumerate(seq):
        try:
            if seq[i:i+3] in start:
                for j in range(i+3, len(seq)):
                    if seq[j:j+3] in stop and (j-i)%3==0:
                        aa_set.add(Seq(seq[i:j+3]).translate().strip('*'))
                        break
        except:
            pass

find_orf(seq)
find_orf(comp_seq)
for seq in aa_set:
    print(seq)
