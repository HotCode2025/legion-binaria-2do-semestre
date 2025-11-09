class Persona2:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}.")
    @property
    def nombre(self):
        print("Estamos usando el metodo GET")
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        print("Estamos usando el metodo SET")
        self._nombre = nombre
    #------------------#
    @property
    def apellido(self):
        print("Estamos usando el metodo GET")
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        print("Estamos usando el metodo SET")
        self._apellido = apellido
    #------------------#
    @property
    def edad(self):
        print("Estamos usando el metodo GET")
        return self._edad
    @edad.setter
    def edad(self, edad):
        print("Estamos usando el metodo SET")
        self._nombre = edad
persona1 = Persona2 ("Ariel","Betancud",41)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#/Clase parte 2/
class Persona2:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}.")
    @property
    def nombre(self):
        print("Estamos usando el metodo GET")
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        print("Estamos usando el metodo SET")
        self._nombre = nombre
    #------------------#
    @property
    def apellido(self):
        print("Estamos usando el metodo GET")
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        print("Estamos usando el metodo SET")
        self._apellido = apellido
    #------------------#
    @property
    def edad(self):
        print("Estamos usando el metodo GET")
        return self._edad
    @edad.setter
    def edad(self, edad):
        print("Estamos usando el metodo SET")
        self._nombre = edad
persona1 = Persona2 ("Ariel","Betancud",41)
print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
persona1.nombre = "Juan Pedro"
print(persona1.nombre)
print(persona1.mostrar_detalles())