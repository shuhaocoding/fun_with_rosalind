from Bio import SeqIO
from Bio.Seq import Seq

fasta_sequences = SeqIO.parse(open("rosalind_splc.txt"),'fasta')
introns = []
for count, fasta in enumerate(fasta_sequences):
    if count == 0:
        fullseq = str(fasta.seq)
    else:
        introns.append(str(fasta.seq))

poslist = []
for seq in introns:
    poslist.append([fullseq.index(seq),fullseq.index(seq)+len(seq)])
poslist.sort()
print(poslist)

newlist = []
if poslist[0][0] != 0:
    newlist.append([0,poslist[0][0]])
for count, pos in enumerate(poslist):
    if count != len(poslist) - 1:
        newlist.append([pos[1],poslist[count+1][0]])
if poslist[len(poslist)-1][1] != len(fullseq):
    newlist.append([poslist[len(poslist)-1][1],len(fullseq)])


exons = []
for pos in newlist:
    exons.append(fullseq[pos[0]:pos[1]])

aaseq = Seq(''.join(exons)).transcribe().translate()
print(aaseq)
