'''
Ejercicio 4: Sumar números pares dentro de un rango
Hacer un programa para sumar números pares dentro de un rango, por ejemplo:
suma de números pares del 2 al 30
suma = 240
'''

def suma_pares(inicio: int, fin: int) -> int:
    if inicio > fin:
        inicio, fin = fin, inicio
    start = inicio if inicio % 2 == 0 else inicio + 1
    return sum(range(start, fin + 1, 2))

print(suma_pares(2, 30))