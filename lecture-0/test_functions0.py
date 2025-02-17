def add_numbers(a,b):
    # Variable local a la función
    
    #global s
    
    # Variable local
    a=a+b
    return a

# Variable global
s=0
x1=45.0
x2=-37.8
result=add_numbers(x1,x2)
print(result)
print(s)
