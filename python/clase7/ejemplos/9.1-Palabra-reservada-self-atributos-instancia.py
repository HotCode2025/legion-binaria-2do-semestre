class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1=Persona("Ariel","Betancud",40)
print(f"El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")
persona2=Persona("Osvaldo","Giordanini",45)
print(f"El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40

print(f"El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

persona1.mostrar_detalle()
persona2.mostrar_detalle()
#Persona.mostrar_detalle() #Si no se pasa referencia, da error