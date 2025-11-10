from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion de objeto clase Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(8, "azul")
cuadrado1.alto = -10
print(cuadrado1.ancho)
print(cuadrado1.alto)

print(f'Calculo del area del cuadrado: {cuadrado1.calcular_area()}')


# MRO = Method Resolution Order

print(Cuadrado.mro()) 

print(cuadrado1)
print("Creacion de objeto clase Rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(3, 9, "verde")
rectangulo1.ancho = 15
print(f'Calculo del area del rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

