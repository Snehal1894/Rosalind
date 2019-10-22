from convert_to_fasta import *


id_seq()

f1 = open("rosalind_grph_updated.txt","r")
lines = f1.readlines()

for i in range(0,len(lines)-1,2):
	id1 = lines[i].rstrip()
	seq=lines[i+1].rstrip()
	seq1=seq[-3:]
	for j in range(0,len(lines)-1,2):
		id2=lines[j].rstrip()
		if(id1!=id2):
			seq=lines[j+1].rstrip()
			seq2=seq[:3]
			if(seq1==seq2):
				print(id1[1:]+" "+id2[1:])
	
