from convert_to_fasta import *

id_seq("rosalind_tran.txt")
f = open("updated.txt","r")
l=f.readlines()
s1=l[1].rstrip()
s2=l[3].rstrip()

transitions=['AG','CT','GA','TC']
transversions=['AC','AT','GC','GT','CA','TA','CG','TG']
tr=0
tv=0
for i in range(len(s1)):
	x=s1[i]+s2[i]
	if(x in transitions):
		tr=tr+1
	if(x in transversions):
		tv=tv+1

print(tr/tv)

