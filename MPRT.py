import requests as r
from Bio import SeqIO
from io import StringIO

def get_sequence(cID):
    baseUrl="http://www.uniprot.org/uniprot/"
    currentUrl=baseUrl+cID+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text)
    text=StringIO(cData)
    f = SeqIO.parse(text,'fasta')
    for fasta in f:
        return str(fasta.seq)
        break
        
def find_motif(seq):
    pos = ''
    for i,aa in enumerate(seq):
        try:
            if aa == 'N' and seq[i+1] != 'P' and (seq[i+2] == 'S' or seq[i+2] == 'T') and seq[i+3] != 'P':
                pos = pos + str(i+1) + ' '
        except:
            pass
    return pos

f=open("output.txt", "w+")
for line in open("rosalind_mprt.txt", "r+"):
    cID = line.strip('\n')
    results = find_motif(get_sequence(cID))
    if results == '':
        continue
    else:
        f.write(cID+'\n'+results+'\n')
