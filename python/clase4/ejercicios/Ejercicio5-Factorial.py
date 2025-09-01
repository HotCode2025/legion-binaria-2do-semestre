'''
Ejercicio 5: Factorial de un número positivo
Hacer un programa para calcular el factorial de un número positivo
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Ingrese un numero postivo:"))

if num < 0:
    print("La operación factorial se define solo para números positivos")


else:
    print(f"El factorial de {num} es {factorial(num)}")