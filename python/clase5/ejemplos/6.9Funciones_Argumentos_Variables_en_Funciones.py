# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: +args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')
