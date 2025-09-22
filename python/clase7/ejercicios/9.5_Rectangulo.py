
# Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base.
# El nombre del método será calcular_area, utilizando la fórmula:
# area = base * altura
# La base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres.


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# Crear tres objetos ingresados por el usuario
rectangulos = []

for i in range(3):
    print(f"\nRectángulo {i+1}:")
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    rect = Rectangulo(base, altura)
    rectangulos.append(rect)

for i, r in enumerate(rectangulos, start=1):
    print(f"Área del rectángulo {i}: {r.calcular_area()}")
