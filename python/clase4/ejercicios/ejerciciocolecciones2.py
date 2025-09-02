#Ejercicio 2: Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 listas y que cree las siguientes listas, en las que no deben haber repeticiones:
#Lista de todas las palabras
#Lista de palabras presentes en la primer lista, pero no en la segunda
#Lista de palabras presentes en la segunda lista, pero no en la primera
#Lista de palabras presentes en ambas listas

lista_a = ["matriz", "flujo", "código", "nodo", "reflejo"]
lista_b = ["reflejo", "nodo", "pantalla", "flujo", "silla"]

lista1 = lista_a + lista_b
print(lista1)
lista2 = []
for item in lista1:
    if item in lista_a and item not in lista_b:
        lista2.append(item)
print(lista2)
lista3 = []
for item in lista1:
    if item in lista_b and item not in lista_a:
        lista3.append(item)
print(lista3)
lista4 = []
for item in lista1:
    if item in lista_a and item in lista_b:
        if item not in lista4:
            lista4.append(item)
print(lista4)