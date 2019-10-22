


def all_combs(l1,n):
	l2=[]
	l3=[]
	l2=l1
	for k in range(n-1):
		for i in range(len(l1)):
			for j in range(len(l2)):
				l3.append(l1[i]+l2[j])
		l2=l3
		l3=[]
	return l2
		

l1="TQGURFPLKADJ"
n=3
res=[]
for i in range(1,n+1):
	res=res+all_combs(list(l1),i)
	

res=sorted(res,key=lambda word:[l1.index(c) for c in word])
for x in res:
	print(x)
