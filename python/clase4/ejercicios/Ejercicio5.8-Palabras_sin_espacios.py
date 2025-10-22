# Ejercicio 5.8: Mostrar una frase sin espacios y contar su longitud

# Definimos una función
def procesar_frase(frase):
    # Quitamos espacios
    frase_sin_espacios = ""
    for letra in frase:
        if letra != " ":
            frase_sin_espacios = frase_sin_espacios + letra

    # Contamos los caracteres
    cantidad = 0
    for letra in frase_sin_espacios:
        cantidad = cantidad + 1

    # Devolvemos los dos resultados
    return frase_sin_espacios, cantidad

#Pedimos que se ingrese la frase
frase = input("Ingrese una frase: ")

# Usamos la función
resultado, total = procesar_frase(frase)

# Mostramos resultados
print("Frase final:", resultado)
print("Número de caracteres:", total)
