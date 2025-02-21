# Ask for number of people
n=int(input('Enter number of people: '))

# Make room in list for n elements
#bmi=[0.0]*n
bmi=[]

# For loop
for i in range(n):
    height=float(input(f'Enter height for person {i+1} in meters: '))
    weight=float(input(f'Enter weight for person {i+1} in kilograms: '))
    #bmi[i]=weight/(height)**2
    bmi.append(weight/(height)**2)
i=0
for b in bmi:
    i=i+1
    if b<18.5:
        print(f'Person {i} weight is low')
        continue
    if 18.5<=b<22.9:
        print(f'Person {i} weight is normal')
        continue    
    
   
    if 22.9<=b<24.9:
        print(f'Person {i} has risk to overweight')    
        continue
    if 24.9<=b<29.9:
        print(f'Person {i} weight is high')
        continue   
    
    if b>=29.9:
        print(f'Person {i} is obese')
        continue

while True:
    pass # No operation
       

print('I\'m ready')

