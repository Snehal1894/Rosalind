
k=21
m=29
n=23

def fact(n):
	res=1
	res=n*(n-1)/2
	return res

den = (k+m+n)*(k+m+n-1)*2
#print(den)
num = 4*(fact(k)+k*(m+n))+3*fact(m)+2*m*n
#print(num)
print(num/den)


