#La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina.
#Los elementos a ingresar deben ser como mínimo 4.
#Estos elementos son los jugadores con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego.

#diccionario en el ejemplo
seleccionArgentina = {
    10: {
        "nombre": "Lionel",
        "apellido": "Messi",
        "edad": 36,
        "altura": 1.70,
        "precio": 50000000,
        "posición": "Delantero"
    },
    11: {
        "nombre": "Ángel",
        "apellido": "Di María",
        "edad": 35,
        "altura": 1.80,
        "precio": 4000000,
        "posición": "Delantero"
    },
     21: {
        "nombre": "Paulo",
        "apellido": "Dybala",
        "edad": 31,
        "altura": 1.77,
        "precio": 20000000,
        "posición": "Delantero"
    },
    19: {
        "nombre": "Nicolás",
        "apellido": "Otamendi",
        "edad": 35,
        "altura": 1.83,
        "precio": 5000000,
        "posición": "Defensor"
    },
    12: {
        "nombre": "Franco",
        "apellido": "Armani",
        "edad": 39,
        "altura": 1.89,
        "precio": 3000000,
        "posición": "Arquero"
    }
}
#Elementos en el ejemplo
print("Jugadores en el ejemplo")
for item, valor in seleccionArgentina.items():
    print(item,valor)
#Elementos nuevos
seleccionArgentina[1] = {
        "nombre": "Emiliano",
        "apellido": "Martínez",
        "edad": 31,
        "altura": 1.95,
        "precio": 25000000,
        "posición": "Arquero"
    }
seleccionArgentina[13] = {
        "nombre": "Cristian",
        "apellido": "Romero",
        "edad": 26,
        "altura": 1.85,
        "precio": 40000000,
        "posición": "Defensor"
}
seleccionArgentina[8] = {
        "nombre": "Marcos",
        "apellido": "Acuña",
        "edad": 33,
        "altura": 1.72,
        "precio": 8000000,
        "posición": "Defensor"
}
seleccionArgentina[7] = {    
        "nombre": "Rodrigo",
        "apellido": "De Paul",
        "edad": 29,
        "altura": 1.80,
        "precio": 30000000,
        "posición": "Mediocampista"
}
#Ejemplos y elementos nuevos
print("4 jugadores agregados")
for item, valor in seleccionArgentina.items():
    print(item,valor)
