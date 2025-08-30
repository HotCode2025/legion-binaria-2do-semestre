# Lista = Ariel, Liliana, Natalia, Osvaldo
# Colecciones en Python

# Las listas es lo que conoce en otros lenguajes como arreglos o vectores

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1]) # Para poner el ultimo elemento de la lista sin saber el largo
print(nombres[-2]) # Para poner el penultimo elemento de la lista sin saber el largo
print(nombres[0:2]) # Imprime desde el 0 al 1 pero no el indice 2
# ir al inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) # Imprime desde el inicio hasta el indice 3
print(nombres[1:]) # Imprime desde el indice 1 hasta el final de la lista
nombres[2] = 'Liliana'
nombres[0] = 'Natalia' # Cambia el valor del indice 0
print(nombres) # Imprime la lista actualizada
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los nombres en la lista")

# Preguntamos cuantos elementos tiene la lista
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)

# Insertamos un elemento en una posicion especifica
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminamos el ultimo elemento
nombres.pop()
print(nombres)

# Eliminamos un indice especifico
del nombres[2]
print(nombres)

# Eliminar, borrar o limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar la lista completa
del nombres
#print(nombres)
