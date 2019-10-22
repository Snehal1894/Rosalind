from Bio.Seq import Seq
from convert_to_fasta import *

id_seq("rosalind_revp.txt")
f = open("updated.txt","r")
l=f.readlines()

seq=l[1].rstrip()
for i in range(4,13):
	for j in range(0,len(seq)-i+1):
		x=seq[j:j+i]
		x=Seq(x)
		y=x.reverse_complement()
		if(x==y):
			print(j+1,i)
