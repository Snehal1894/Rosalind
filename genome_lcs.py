
def id_seq(filename):	
	lg=9999
	s=[]
	f1 = open(filename,"r")
	lines = f1.readlines()
	ids=""
	for i in range(0,len(lines)):
		l=lines[i].rstrip()
		if ">" in l :
			if (ids!="" and seq!=""):
				s.append(seq)
			ids = l
			seq=""
		else:
			seq=seq+l
	s.append(seq)
	return s


def get_lcs(seqs,s):
	for n in range((len(s)),0,-1):
		for i in range(0,len(s)-n):
			ln=s[i:i+n+1]
			matching = [x for x in seqs if ln in x]
			if(len(matching)==len(seqs)):
				return ln

seqs=id_seq("rosalind_lcsm.txt")
s=min(seqs,key=len)
ln=get_lcs(seqs,s)
print(ln)




