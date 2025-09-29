class Persona: #Creamos una clase
    def __init__(self,nombre,apellido,edad):# se lo llama metodo Init Dumber
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
# Marcamos punto de ruptura y hacemos Debug de los objetos
        
persona1 = Persona('Ariel', 'Betancud', 40) #Necesitamos enviar argumentos Debug = persona1 = <__main__.Persona object at 0x00000281A39C78C0>
        
print(persona1.nombre)  #Ariel
print(persona1.apellido)  #Betancud
print(persona1.edad)  #40

persona2 = Persona('Osvaldo','Giordanini', 45) #Debug = persona2 = <__main__.Persona object at 0x00000222549D0A50>
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}') #El objeto 2 de la clase persona: Osvaldo Giordanini Su edad es: 45