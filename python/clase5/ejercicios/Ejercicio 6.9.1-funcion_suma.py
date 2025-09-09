# Ejercicio 6.9.1: Crear una función para sumar los valores recibidos de tipo numéricos,
# utilizando argumentos variables *args como parámetro de la función
# y agregar como resultado la suma de todos los valores pasados como argumentos.

def sumar_valores(*args):
   
    suma = 0  
    for numero in args: 
        suma += numero 
    return suma 

# Probamos la función

print("El resultado de la suma es: ", sumar_valores(1,5,6))
print("El resultado de la suma es: ", sumar_valores(39,22,7))
print("El resultado de la suma es: ", sumar_valores(2,5,80,13,1,52))