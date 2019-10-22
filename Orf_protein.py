from Bio.Seq import Seq
from convert_to_fasta import *

global prts

def frames(seq):
	for i in range(0,3):
		seq1=seq[i:]
		lg=len(seq1)-len(seq1)%3
		get_protein(seq1[0:lg])


def get_protein(seq):
	x=seq.translate()
	arr=str(x).split("*")
	#print(x)
	for i in range(0,len(arr)-1):
		s=arr[i]
		if "M" in s:
			idx=[i for i, a in enumerate(s) if a == "M"]
			for dx in idx:
				if s[dx:] not in prts:
					prts.append(s[dx:])

prts=list()	
id_seq("rosalind_orf.txt")
f = open("updated.txt","r")
l=f.readlines()
seq=Seq(l[1].rstrip())
r_seq= seq.reverse_complement()
frames(seq)
frames(r_seq)

#print(prts)
for p in prts:
	print(p)


