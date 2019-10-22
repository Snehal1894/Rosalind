import re
import requests as r
from Bio import SeqIO
from io import StringIO


u_ids=["P01045_KNH2_BOVIN","B2G8U6","P01046_KNL1_BOVIN","Q82ZQ1","A2Z669","A6WKC3","P21809_PGS1_BOVIN","Q181G8","P01880_DTC_HUMAN","A1TJ10","P10761_ZP3_MOUSE","O74366"]
for cID in u_ids:
	
	finds=list()
	baseUrl="http://www.uniprot.org/uniprot/"
	currentUrl=baseUrl+cID+".fasta"
	response = r.post(currentUrl)
	cData=''.join(response.text)
	b=cData.find("\n")
	#print(cData[:b])
	seq=cData[b:].replace("\n","")
	res=0
	while(re.search(r'N[^P][ST][^P]', seq)!=None):
		idx=re.search(r'N[^P][ST][^P]', seq)
		st=idx.span()[0]
		res=res+(st+1)
		finds.append(res)
		#print(str(res)+" ",end='')
		#print("st:",st)
		seq=seq[st+1:]
	if(len(finds)!=0):
		print("\n"+cID)
		for f in finds:
			print(str(f)+" ",end='')
