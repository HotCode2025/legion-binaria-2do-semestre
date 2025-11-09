'''
Ejercicio 1: Eliminar duplicados de una lista
Escriba un programa donde tenga una lista y que a continuación
elimine los elementos repetidos, por último mostrar la lista.
'''

#Creamos una lista
lista = [1, 1, 2, 2, 6, 6, 8, 9, 3, 4, 4, 5, 1]
listaSinDuplicados = list(set(lista)) #Eliminamos los elementos repetidos

print(listaSinDuplicados) #Mostramos la lista sin duplicados


