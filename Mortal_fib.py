
n=90
m=20
mature=[0]*n
kid=[0]*n
mature[1]=1
kid[0]=1
def fibo():
	for i in range(2,m):
		mature[i]=mature[i-1]+mature[i-2]
		kid[i]=kid[i-1]+kid[i-2]

def update_m_k():
	for i in range(m,n):
		mature[i]=mature[i-1]+mature[i-2]-kid[i-m]
		kid[i]=mature[i-1]

	
fibo()
update_m_k()
#print(mature)
#print(kid)

print(mature[n-1]+kid[n-1])
