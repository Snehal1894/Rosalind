
def id_seq(filename):	
	f1 = open(filename,"r")
	lines = f1.readlines()
	f2 = open("updated.txt","w")
	ids=""
	for i in range(0,len(lines)):
		l=lines[i].rstrip()
		if ">" in l :
			if (ids!="" and seq!=""):
				f2.write(ids+"\n"+seq+"\n")
			
			ids = l
			seq=""
		else:
			seq=seq+l
	f2.write(ids+"\n"+seq+"\n")
	
	
