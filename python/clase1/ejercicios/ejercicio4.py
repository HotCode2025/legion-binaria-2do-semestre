'''
ejercicio 4:
1. Dada la siguiente tupla.
tupla = (13, 1, 8, 3, 2, 5, 8)
2. Crea una lista que solo incluya los números menores a 5 e imprime la lista
'''

# tupla inicial
tupla = (13,1,8,3,2,5,8)

# variable inicial de lista
lista_tupla = []

# si n < 5, lo agrego al final de lista_tupla
for n in tupla:
    if n < 5:
        lista_tupla.append(n) 
print(lista_tupla)