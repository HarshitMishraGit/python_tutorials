'''recursions'''
def fact(n):
    '''this is a simple example of recursions'''
    if n==0:
        return 1
    
    return n*fact(n-1)

def fact2(n):
    '''this is a simple example using iterative approach'''
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
            
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input('Enter a number: '))
print(fibo(n))