'''
TIPO SET O CONJUNTO
'''


# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Usamos la funcon len = length significa largo

# Revisa si un elemento existe dentro de set
print('Marte' in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)

# Eliminar elementos, puede arrojar error si el elemento no existe
planetas.remove('Venus')
print(planetas)

# Eliminar un elemento sin arrojar error si no existe
planetas.discard('Tierra') # discard no arroja error si no existe

# Limpiar el set
planetas.clear()
print(planetas) 

# Eliminar set o conjunto
# del planetas
# print(planetas)  # Esto generará un error porque planetas ya no existe