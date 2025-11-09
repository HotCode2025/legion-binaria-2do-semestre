#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa.
#Investigar las formulas.

def ctof (c):
    f = c * (9 / 5) + 32
    return f
def ftoc (f):
    c = (f - 32) * (5 / 9)
    return c

#Ejemplo con 100°C y F
#print(ctof(100))
#print(ftoc(100))

print("Ingrese 1 o 2, segun la conversion que desee:")
print("1: °C a °F")
print("2: °F a °C")
opcion = input("1 o 2:")

if opcion == "1":
    celsius = float(input("Ingrese el valor en °C: "))
    print(celsius, "°C equivalen a ",ctof(celsius),"°F.")
else:
    if opcion == "2":
        fahr = float(input("Ingrese el valor en °F: "))
        print(fahr, "°F equivalen a ",ftoc(fahr),"°C.")
