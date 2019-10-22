
n=1
l1='DNA'
l2=[]
l3=[]
l2=l1

for k in range(n-1):
	for i in range(len(l1)):
		for j in range(len(l2)):
			l3.append(l1[i]+l2[j])
	l2=l3
	l3=[]
	
for x in l2:
	print(x)

