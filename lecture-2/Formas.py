from math import pi

# Define clase Circulo con 3 atributos
class Circulo:
    # Función constructor, se llama cuando se crea el objeto
    # El constructor define 3 atributos
    def __init__(me,radioi,centroXi,centroYi):
        me.radio=radioi
        me.centroX=centroXi
        me.centroY=centroYi
        

    # Se definen dos métodos para la clase Circulo
    def area(self):
        return pi*self.radio**2
    
    def perimetro(this):
        return 2*pi*this.radio
    
class Rectangle:
    pass