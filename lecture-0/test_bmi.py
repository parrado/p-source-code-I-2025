# Ask for number of people
n=int(input('Enter number of people: '))

# Make room in list for n elements
bmi=[0.0]*n

# For loop
for i in range(n):
    height=float(input(f'Enter height for person {i+1} in centimeters: '))
    weight=float(input(f'Enter weight for person {i+1} in kilograms: '))
    bmi[i]=weight/(height/100)**2

i=0
for b in bmi:
    if b<18.5:
        print(f'Person {i+1} weight is low')
    if 18.5<=b<22.9:
        print(f'Person {i+1} weight is normal')    
    
   
    if 22.9<=b<24.9:
        print(f'Person {i+1} has risk to overweight')    

    if 24.9<=b<29.9:
        print(f'Person {i+1} weight is high')   
    
    if b>=29.9:
        print(f'Person {i+1} is obese')
    
    i=i+1

