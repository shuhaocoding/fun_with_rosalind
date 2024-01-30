from Bio.Seq import Seq
s = input()
print(Seq(s).translate(to_stop=True))