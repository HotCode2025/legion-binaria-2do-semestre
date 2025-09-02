"""
Ejercicio 3: Insertar elementos y ordenarlos
Pedir números y meterlos en una lista, cuando el usuario
introduzca un número 0, nuestro programa dejaría de insertar.
Por último, mostrar los números ordenados de menor a mayor
"""

lista = []

while True:
    number = int(input("Ingrese un numero: "))
    if number == 0:
        break
    else:
        lista.append(number)

lista.sort()
print(lista)