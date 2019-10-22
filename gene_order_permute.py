from itertools import permutations

n=5
l=list(permutations(range(1,n+1)))
print(len(l))
for i in l:
	for j in i:
		print(str(j)+" ",end='')
	print("\n")
