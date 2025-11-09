#Colecciones en Python
nombres = ["Naty","Osvaldo","Lily", "Ariel"]
print(nombres)
#Agregar elementos
nombres.append("Marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)
#Concatenar listas
lista1 = [1,2,3]
lista2 = [4,5,6,1,1,1]
lista3 = lista1+lista2
print(lista3)
#Agregar varios elementos
lista3.extend([7,8,9])
print(lista3)
#Ubicar el indice de un valor
print(lista3.index(5))
#--
#print(lista3.index(0)) -> error porque no esta presente
#--
#Ver cuantos valores iguales hay en una lista
print(lista3.count(1))
#Invertir lista
lista3.reverse()
print(lista3)
#Multiplicar una lista repitiendo elementos
lista3 = lista3*2
print(lista3)
#Metodos de ordenamiento sort
#Ascendente
lista3.sort()
print(lista3)
#Descendente
lista3.sort(reverse=True)
print(lista3)