from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

print("Creacion de objeto clase Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(8, "Azul")
cuadrado1.alto = 7
# cuadrado1.ancho = 7
# print(cuadrado1.alto)
# print(cuadrado1.ancho)
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
# print(Cuadrado.mro()) 

#Se deben quitar el Metodo Setter de los atibutos al y ancho para que sean Read-Only(solo lectura)

print(cuadrado1)
print("Creacion de objeto clase Rectangulo")
rectangulo1 = Rectangulo(3, 9, "verde")
rectangulo1.ancho = 8
print(f"Calculo del area del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

# figura1 = FiguraGeometrica() No se puede instanciar, es abstracta
print(Cuadrado.mro())