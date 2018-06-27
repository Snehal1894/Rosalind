def fibonacci(n,p):
    if (n==1 or n==2):
        return 1
    else:
        return p*fibonacci(n-2,p)+fibonacci(n-1,p)
    
p=2
n=36
print fibonacci(35,4)
    
