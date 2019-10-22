import math

def binsearch(A,l,r,x):
	mid= math.ceil((l+r)/2)
	if(r<l):
		return -2
	if(x<A[mid]):
		return binsearch(A,l,mid-1,x)
	elif(x>A[mid]):
		return binsearch(A,mid+1,r,x)
	else:
		return mid
		

f=open("rosalind_bins.txt","r")	
lines=f.readlines()	
A=lines[2].rstrip().split(" ")

new_A=[]
for i in A:
	if(not (i in new_A)):
		new_A.append(i)
	else:
		new_A.append(" ")
	
src=lines[3].rstrip().split(" ")

res=[]
res1=[]
for x in src:
	res.append(binsearch(new_A,0,len(A)-1,x)+1)
	try:
		res1.append(A.index(x)+1)
	except ValueError:
		res1.append(-1)
		
print(len(res)," ",len(res1))
print(res==res1)

for j in range(len(res)):
	if(res[j]!=res1[j]):
		print(j," ",res[j]," ",res1[j])





