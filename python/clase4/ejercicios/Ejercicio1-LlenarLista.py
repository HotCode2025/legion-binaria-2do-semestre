# Ejercicio 1: Llenar una lista con números del 1 al 50, luego mostra la lista con el bucle for, los elementos deben mostrarse de la siguiente forma: 1-2-3-4-...-50

# Crear lista con números del 1 al 50
numeros = list(range(1, 51))

# Mostrar los elementos con guiones
for i in range(len(numeros)):
    if i < len(numeros) - 1:
        print(numeros[i], end="-")
    else:
        print(numeros[i])
