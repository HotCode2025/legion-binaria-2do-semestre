#Ejercicio 4: Calculadora de Impuestos
#Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado (IVA)
#Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
#Proporcione el pago sin impuesto: 1000
#Proporcione el monto del impuesto: 21%
#Pago con impuesto: xxxxxxx

def calcimp (monto, impuesto):
    total = monto + monto*(impuesto/100)
    return total

print(f"El monto con impuestos es: {calcimp(1000, 21):.2f}")