from cmath import sqrt

def myRoots(p: list):
    a=(-p[1]+sqrt(p[1]**2-4*p[0]*p[2]))/(2*p[0])
    b=(-p[1]-sqrt(p[1]**2-4*p[0]*p[2]))/(2*p[0])
    
    return a,b

# p=[]

# p.append(float(input('Ingrese coeficiente a: ')))
# p.append(float(input('Ingrese coeficiente b: ')))
# p.append(float(input('Ingrese coeficiente c: ')))
# (r1,r2)=myRoots(p)
# print(f'Raiz 1: {r1},Raiz 2: {r2}')
# r=myRoots(p)
# print(f'Raiz 1: {r[0]},Raiz 2: {r[1]}')

a=(float(input('Ingrese coeficiente a: ')))
b=(float(input('Ingrese coeficiente b: ')))
c=(float(input('Ingrese coeficiente c: ')))

p=(a,b,c)

r=myRoots(p)
print(f'Raiz 1: {r[0]},Raiz 2: {r[1]}')

p=25
r=myRoots(p)