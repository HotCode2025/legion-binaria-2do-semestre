# Ejercicio 7.1: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función.


def multiplicar_valores(*args):
   
    if not args:  # Un if para que retorne 0 si no se le da ningun argumento
        return 0   

    producto = 1  # Comenzamos en 1 porque es el elemento neutro de la multiplicación
    for numero in args:  # Recorremos cada valor recibido y vamos multiplicando
        producto *= numero  
    return producto 

entrada = input("Ingresa números separados por espacio (maximo 10): ")

# Convertimos esa entrada en una lista de enteros
numeros = [int(x) for x in entrada.split()]

# Definimos el límite de números permitidos
LIMITE_NUMEROS = 10

# Verificamos si la cantidad de números ingresados supera el límite
if len(numeros) > LIMITE_NUMEROS:
    print(f"Error: Has ingresado {len(numeros)} números. El límite es {LIMITE_NUMEROS}.")
else:
    # Si la cantidad es válida, llamamos a la función
   resultado = multiplicar_valores(*numeros)

   print("El resultado de la multiplicación es:", resultado)