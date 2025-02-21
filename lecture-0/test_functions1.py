from random import random

def dotProduct(x,y):
    if len(x) !=len(y):
        raise ValueError('Arrays must have same size') 
    n=len(x)
    acc=0.0 # local variable
    for i in range(n):        
        #acc+=x[i]*y[i] #acc=acc+x[i]*y[i]
        #acc=acc+x[i]*y[i]
        acc+=x[i]*y[i]
    return acc



n=1000
a=[0.0]*n
b=[]


for i in range(n):
    a[i]=random()
    b.append(random())

a=[1,2,3]
b=[4,5,6,8]

dot=dotProduct(a,b)

print(f'Dot product is: {dot}')

