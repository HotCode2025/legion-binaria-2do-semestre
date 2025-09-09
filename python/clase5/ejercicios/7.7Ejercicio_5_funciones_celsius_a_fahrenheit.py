#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa.
#Investigar las formulas.

def ctof (c):
    f = c * (9 / 5) + 32
    return f

def ftoc (f):
    c = (f - 32) * (5 / 9)
    return c

#print(ctof(100))

#100°C equivale a 212°F

#print(ftoc(100))

#100°F equivale a 93.3°C
