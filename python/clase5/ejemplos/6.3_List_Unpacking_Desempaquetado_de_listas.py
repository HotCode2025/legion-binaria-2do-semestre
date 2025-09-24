# Comenzamos con Funciones
# mi_funcion() # No se puede llamar antes de definir a una función
#Definimos una funcion
def mi_funcion(): # Para identificar a la función utilizamos paréntesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion() # Estamos llamando a la función
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o lista Unpacking
def show(name, lastName):
    print(name+' '+ lastName)
person = ["Lucia", "Farina"]
show(person[0], person[1]) #pasamos uno por uno los datos de la lista a la función
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Jackeline", "Rodriguez") # desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lazo", "name": "Johana"}
show(**person3)