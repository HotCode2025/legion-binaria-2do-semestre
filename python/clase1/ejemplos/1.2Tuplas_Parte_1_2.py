'''
Tuplas parte 1 y 2
'''

# Definimos una TUPLA
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utlizaremos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ('papa',) # Una tupla necesita aunquesea un elemento con coma
# De lo contrario solo seria un tipo str cadena
print(verduras)

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end =' ') # Print esta usando \n para saltos de líneas

cosinaLista = list(cocina)
cosinaLista[0] = 'Plato'
cocina = tuple(cosinaLista) # Convertimos la lista de nuevo a tupla
print('\n', cocina)

# del cocina # esto es para eliminar una tupla
