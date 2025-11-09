class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter y Setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Getter y Setter para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad
        
    def mostrar_datos(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")
    
    def __str__(self): # override = sobreescritura
        return f"Persona: {self._nombre}, {self._edad}"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    # Getter y Setter para sueldo
    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        self._sueldo = nuevo_sueldo
        
    def mostrar_datos(self):
        super().mostrar_datos()  # Llama al método de la clase padre
        print(f"Sueldo: {self._sueldo}")
    
    def __str__(self): # override = sobreescritura
        return f"Empleado: {self._nombre}, {self._edad}, {self._sueldo}"


# Crear objeto
empleado1 = Empleado('Ariel', 40, 75000)
print("Datos del empleado 1:")
empleado1.mostrar_datos()

# Modificar datos
empleado1.nombre = 'Carlos'
empleado1.edad = 45
empleado1.sueldo = 82000

print("\nDatos del empleado 1 modificados:")
empleado1.mostrar_datos()

# Crear otro objeto
empleado2 = Empleado('Johana', 29, 60000)
print("\nDatos del empleado 2:")
empleado2.mostrar_datos()

# metodo dunder str
print("\nEmpleado 1:", empleado1)
print("Empleado 2:", empleado2)