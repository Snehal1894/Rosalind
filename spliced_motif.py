from convert_to_fasta import *

id_seq("rosalind_sseq.txt")
f = open("updated.txt","r")
l=f.readlines()
seq=l[1].rstrip()
motif=l[3].rstrip()
ln=0
j=0
for c in motif:
	i = seq.find(c)
	print(i+ln+1,end=" ")
	ln=ln+i+2
	seq=seq[i+2:]

	

