from random import random

nData=10000
data=[]
for n in range(nData):
    data.append(random())

print(f'Mean is: {myGeometricMean(data)}')