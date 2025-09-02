# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lsita con los números del 1 al 10, luego modificarlos
# elementos de la lista multiplicados por un valor ingresado por el usuario.
lista = list(range(1, 11))
print("Lista original:")
for i in lista:
    print(i, end=" ")
valor = int(input('\nDigite un valor a multiplicar por favor:'))
for indice, i in enumerate(lista):
    lista[indice] = i * valor

print(f'Lista final con los elemetnos multiplicados por {valor}:')
for i in lista:
    print(i, end=' ')