class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property
    def nombre(self):
        print("Estamos utilizando el método get de nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Estamos utilizando el método set de nombre")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.nombre)
persona1.nombre = "Juan"
persona1.mostrar_detalles() 

# TAREA: crear 3 objetos más, utilizando los metodos getter y setter, para modificar y mostrar los cambios con el metodo mostrar_detalles()
persona2 = Persona2("María", "López", 30)
persona3 = Persona2("Carlos", "García", 25)
persona4 = Persona2("Lucía", "Martínez", 35)

# Modificamos usando setters
persona2.nombre = "Mariana"
persona2.edad = 31

persona3.apellido = "Gómez"
persona3.nombre = "Carlitos"

persona4.nombre = "Lu"
persona4.apellido = "Márquez"
persona4.edad = 36

# Mostramos los resultados
persona2.mostrar_detalles()
persona3.mostrar_detalles()
persona4.mostrar_detalles()
