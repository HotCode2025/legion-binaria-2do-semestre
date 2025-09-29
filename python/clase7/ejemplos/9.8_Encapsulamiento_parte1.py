#Encapsulamiento Parte1
class Persona: 
    def __init__(self,nombre,apellido,dni,edad,*args,**kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.args = args
        self.kwargs = kwargs
    
    def mostrar_detalle(self): 
         print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')
         
persona1 = Persona('Ariel', 'Betancud', 32456987, 40) #Agregamos el argumento dni a persona1
        
#print(persona1.nombre)  
#print(persona1.apellido) 
#print(persona1.edad)  
print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')


persona2 = Persona('Osvaldo','Giordanini', 30321456, 45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

# Los atributos son: características
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()  # La referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

persona1.telefono = '44445555289'
print(f'Este es el teléfono de: {persona1.nombre} {persona1.telefono}') 

persona3 = Persona('Rogelio', 'Romero', 35789465, 22 , 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen',Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni)# Esto no se debe utilizar (esta encapsulado), esto dice que desconocemos Python.