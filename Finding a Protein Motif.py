import requests as r
from Bio import SeqIO
from io import StringIO

# Define a function to get the protein sequence for a given uniprot ID
def get_sequence(cID):
    # Download the data from URL
    baseUrl="http://www.uniprot.org/uniprot/"
    currentUrl=baseUrl+cID+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text)
    text=StringIO(cData)
    # Parse the data
    fa = SeqIO.parse(text,'fasta')
    for fasta in fa:
        return str(fasta.seq)
        break

# Define a function to identify the N-glycosylation motif in a given sequence
def find_motif(seq):
    pos_string = ''
    for i, aa in enumerate(seq):
        try:
            if aa == 'N' and seq[i+1] != 'P' and (seq[i+2] == 'S' or seq[i+2] == 'T') and seq[i+3] != 'P':
                pos_string = pos_string + str(i+1) + ' '
        except:
            pass
    return pos_string

# For each ID in the input file, get the positions and write them to an output file
f=open("output.txt", "w+")
for line in open("rosalind_mprt.txt", "r+"):
    cID = line[:6]
    results = find_motif(get_sequence(cID))
    if results == '':
        continue
    else:
        f.write(cID+'\n'+results+'\n')
f.close()
