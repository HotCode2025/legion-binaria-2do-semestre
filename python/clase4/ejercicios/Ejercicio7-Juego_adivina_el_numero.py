""" 
Ejercicio 7: juego adivina el numero.
Realizar un juego para adivinar un numero. Para ello se debe generar
un numero aleatorio entre 1 - 100, y luego ir pidiendo numeros indicando
"es mayor" o "es menor" segun sea mayor o menor con respecto a N. El proceso
termina cuando el usuario acierta y mostramos el numero de intentos.
"""

import random

def adivina_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0

    while True:
        intentos += 1
        numero_ingresado = int(input("Ingrese un número entre 1 y 100: "))
        if numero_ingresado == numero_aleatorio:
            print(f"¡Adivinaste el numero en {intentos} intentos!")
            break
        elif numero_ingresado < numero_aleatorio:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")

adivina_numero()