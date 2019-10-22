from Bio.Seq import Seq
from convert_to_fasta import *

id_seq("rosalind_splc.txt")
f = open("updated.txt","r")
l=f.readlines()
seq=l[1].rstrip()
print(seq)
for i in range(3,len(l),2):
	seq=seq.replace(l[i].rstrip(),"")
seq=Seq(seq)
print(seq.translate())
