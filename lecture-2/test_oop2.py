class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    # Define age como una propiedad de solo lectura (decorador property)
    @property
    def age(self): # Método getter para obtener el valor del atríbuto
        return self.__age

    # Con el setter se puede tener control de qué valores
    # son válidos para la propiedad
    @age.setter
    def age(self,age):
        if age>=0:
            self.__age=age
    
    # Método para imprimir nombre
    def sayHi(self):
        print(f'Hi my name is {self.name} and  I\'m {self.__age} years old')

    
p0=Person("Esteban",33)
nombre=input('Ingrese el nombre: ')
edad=int(input('Ingrese la edad: '))
p0.name=nombre
p0.age=edad







p1=Person('Cristina',20)


p0.sayHi()
p0.age=-19
print(p0.age)
        