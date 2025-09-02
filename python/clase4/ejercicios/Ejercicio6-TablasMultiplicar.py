'''
Ejercicio 6: Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10.
Por ejemplo: Si sigita el 5, 
la lista tendrá: 5,10,15,20,25,30,35,40,45,50
'''

def pedir_entero(msg="Digite un número: "):
    while True:
        dato = input(msg).strip()
        try:
            return int(dato)
        except ValueError:
            print("Entrada inválida. Ingrese un entero, por favor.")

def tabla_multiplicar(n: int) -> list[int]:
    return [n * i for i in range(1, 11)]

if __name__ == "__main__":
    n = pedir_entero()
    tabla = tabla_multiplicar(n)
    print(tabla)