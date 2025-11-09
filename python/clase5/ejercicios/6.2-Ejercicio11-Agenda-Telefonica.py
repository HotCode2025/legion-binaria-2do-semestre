# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

agenda = {} 
while True:
    print("\nAgenda Telefónica")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado.")
    
    elif opcion == '2':
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} borrado.")
        else:
            print(f"El contacto {nombre} no existe.")
    
    elif opcion == '3':
        if agenda:
            print("\nContactos existentes:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            print("No hay contactos en la agenda.")
    
    elif opcion == '4':
        print("Saliendo de la agenda telefónica ¡Gracias!.")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")