""" 
Repaso tipo set o conjunto
"""

#Para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)

conjunto1.add('Hola')
print(3 not in conjunto1) #Preguntamos si el número 3 no está en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1) #Nos devuelve como respuesta un booleano

#Operaciones de conjuntos
conjunto3 = conjunto1 | conjunto2 #La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Qué elementos tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Elementos que están en el conjunto1 pero no en el conjunto2
print(conjunto3) 

conjunto3 = conjunto2 - conjunto1 
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #Elementos que no se repiten en ambos conjuntos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Preguntamos si un conjunto es subconjunto detro de otro (si conjunto2 es subconjunto de conjunto3)
print(conjunto1.issubset(conjunto3)) 
print(conjunto3.issubset(conjunto2))
print(conjunto3.issubset(conjunto1)) 

print(conjunto3.issuperset(conjunto2)) #Preguntamos si un conjunto es un superconjunto de otro
print(conjunto3.issuperset(conjunto1)) 
print(conjunto2.issuperset(conjunto3)) 
print(conjunto1.issuperset(conjunto3)) 

#Cómo saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) 

#Convertir un conjunto totalmente inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea inmutable (No se puede agregar, modificar o eliminar elementos del conjunto)