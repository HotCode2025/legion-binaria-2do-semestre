"""
Crear la clase cubo con los atributos: ancho, alto y profundidad. Con un metodo
llamado calcular_volumen, utilizando la fórmula: volumen = ancho * alto * profundidad.
Que el usuario ingrese los valores.
"""

class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

# Crear un cubo
ancho = float(input("Ingrese el ancho del cubo: "))
alto = float(input("Ingrese el alto del cubo: "))
profundidad = float(input("Ingrese la profundidad del cubo: "))
cubo = Cubo(ancho, alto, profundidad)

# Calcular el volumen
volumen = cubo.calcular_volumen()
print(f"El volumen del cubo es: {volumen}")