def imprimir_descendente(n):
    if n <= 0:
        return
    print(n)
    imprimir_descendente(n - 1)


# Ejemplos
print("Ejemplo con n = 5:")
imprimir_descendente(5)

print("\nEjemplo con n = 3:")
imprimir_descendente(3)

print("\nEjemplo con numero negativo")
imprimir_descendente(-2)  # No tiene que imprimir nada
