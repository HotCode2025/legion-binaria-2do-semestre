#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

personajes = []
#personajes.append({"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del norte"})
#personajes.append({"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"})
#personajes.append({"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"})

def cargar(lista,nombre,clase,raza):
    lista.append({"Nombre": nombre, "Clase": clase, "Raza": raza})

cargar(personajes,"Aragon","Guerrero","Dunadan del norte")
cargar(personajes,"Gandalf","Mago","Istar")
cargar(personajes,"Legolas","Arquero","Elfo Sindar")

print(personajes)
for item in personajes:
    print(item)