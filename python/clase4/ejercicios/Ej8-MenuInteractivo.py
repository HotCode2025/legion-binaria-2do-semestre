# Hacer un programa que simule un cajero automatico con un saldo inicial de 1000$ y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

# Cajero automático
saldo = 1000  # saldo inicial

while True:
    print("\n=== Cajero Automático ===")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        ingreso = float(input("¿Cuánto dinero deseas ingresar?: "))
        saldo += ingreso
        print(f"Has ingresado {ingreso}$. Tu nuevo saldo es {saldo}$.")

    elif opcion == "2":
        retiro = float(input("¿Cuánto dinero deseas retirar?: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Has retirado {retiro}$. Tu nuevo saldo es {saldo}$.")

    elif opcion == "3":
        print(f"Tu saldo disponible es {saldo}$.")

    elif opcion == "4":
        print("Gracias por usar el cajero automático.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
