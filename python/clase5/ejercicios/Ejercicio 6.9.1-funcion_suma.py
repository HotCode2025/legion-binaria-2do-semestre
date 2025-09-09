# Ejercicio 6.9.1: Crear una función para sumar los valores recibidos de tipo numéricos,
# utilizando argumentos variables *args como parámetro de la función
# y agregar como resultado la suma de todos los valores pasados como argumentos.

def sumar_valores(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

# Pedimos al usuario que ingrese los números separados por espacios
entrada = input("Ingresa números separados por espacio (máximo 5): ")
2
numeros = [int(x) for x in entrada.split()]

# Definimos el límite de números permitidos
LIMITE_NUMEROS = 10

# Verificamos si la cantidad de números ingresados supera el límite
if len(numeros) > LIMITE_NUMEROS:
    print(f"Error: Has ingresado {len(numeros)} números. El límite es {LIMITE_NUMEROS}.")
else:
    # Si la cantidad es válida, llamamos a la función
    resultado = sumar_valores(*numeros)
    print("La suma de los valores es:", resultado)