'''
Ejercicio 10: No repetir caracteres
Hacer un programa que pida una cadena por teclado, 
luego meter los caracteres en un lista sin repetir caracteres.
'''

cadena = input("Introduce una cadena: ")  #Pedimos una cadena por teclado

lista_sin_repetir = list(set(cadena))   

print("La lista sin repeticiones es:", lista_sin_repetir) #Mostramos la lista sin repeticiones

