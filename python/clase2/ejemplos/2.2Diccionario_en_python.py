'''
DICCIONARIOS EN PYTHON
'''

# 'Maradona':10 un diccionario esta compuesto por dos elementos
# La clave es 'Maradona' y el valor es 10
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Vase de Datos',
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Aceder a un diccionario con la llave(key)
print(diccionario['IDE']) 

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['Ide'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elemtnos
for termino in diccionario:
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una función
    print(termino)  # Muestra solo las lalves

for valor in diccionario.values(): # Usamos una funcion para acceder al diccionario
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario)  # Devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()


# ELiminar diccionario
# del diccionario # el diccionario ya no existe