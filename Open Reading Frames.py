from Bio import SeqIO
from Bio.Seq import Seq

# Parse the sequences
seqrecords = list(SeqIO.parse(open("rosalind_orf.txt"), 'fasta'))
seq = str(seqrecords[0].seq)
comp_seq = str(Seq(seq).reverse_complement())

# Define the start and stop codons
start = ["ATG"]
stop = ["TAA","TAG","TGA"]

# Generate a set for storing putative ORF sequences
orf_set = set()
# Define a function to identify ORFs
def find_orf(seq):
    for i, base in enumerate(seq):
        try:
            if seq[i:i+3] in start: # find start codons
                for j in range(i+3, len(seq)):
                    if seq[j:j+3] in stop and (j-i)%3==0: # find stop codons
                        orf_set.add(Seq(seq[i:j+3]).translate().strip('*'))
                        break
        except:
            pass

# Run the function on both sense and antisense strands
find_orf(seq)
find_orf(comp_seq)
for orf in orf_set:
    print(orf)
