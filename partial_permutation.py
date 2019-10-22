
n=9
k=91
res=1
for i in range(n):
	res = (res * k)%1000000
	k-=1

print(res)


