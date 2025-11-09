def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
resultado = factorial(5)
print(f"El factorial del numero 5 es: {resultado}")

numUsuario = int(input("Ingrese un numero entero para calcular su factorial ->->-> "))
print(f"El factorial del numero {numUsuario} es: {factorial(numUsuario)}")