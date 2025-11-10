from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creacion de objeto clase Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(8, "Azul")
cuadrado1.alto = 7
cuadrado1.ancho = 7
# print(cuadrado1.alto)
# print(cuadrado1.ancho)

print("Área del cuadrado:", cuadrado1.calcular_area())
print(cuadrado1)

# MRO = Method Resolution Order
# print(Cuadrado.mro()) 


print("Creacion de objeto clase Rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(3, 9, "verde")
rectangulo1.ancho = 8

print("Área del rectángulo:", rectangulo1.calcular_area())
print(rectangulo1)


