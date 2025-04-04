from math import pi

# Base/parent class is abstract
class Shape:
    def __init__(self,centerX,centerY):
        self._centerX=centerX
        self._centerY=centerY
    
    # area must be implementd by child classes (Abstract method)
    # (polymorphism)
    def area(self):
        pass
    
    def showCoordinates(self):
        print(f'My coordinates are ({self._centerX},{self._centerY})')

# Circle inherits from Shape
class Circle(Shape):
    
    def __init__(self,centerX,centerY,radius):
        super().__init__(centerX,centerY) # Call constructor of Shape
        self.radius=radius
        
    # Implement area 
    def area(self):
        return pi*self.radius**2

# Triangle inherits from Shape
class Triangle(Shape):
    def __init__(self,centerX,centerY,base,height):
        super().__init__(centerX,centerY)
        self.height=height
        self.base=base
        

    def area(self):
        return self.base*self.height/2
    
    def coord(self):
        print(self._centerX,self._centerY)
    
# Object Circle of radius 1    
myCircle0=Circle(-2.0,2.0,1.0)

# Object Triangle of base 5 and heigh 3
myTriangle0=Triangle(0.1,0.1,5.0,3.0)

aCircle=myCircle0.area()
aTriangle=myTriangle0.area()

print(f'El área del círculo es: {aCircle}')
print(f'El área del triángulo es: {aTriangle}')
myCircle0.showCoordinates()
myTriangle0.showCoordinates()
myTriangle0.coord()

