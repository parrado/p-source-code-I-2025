from random import uniform



nData=10000
data=[]
for n in range(nData):
    data.append(uniform(0.1,1))

print(f'Mean is: {myGeometricMean(data)}')
