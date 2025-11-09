class Aritmetica:
    """
    DocString
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    def sumar(self):
        return self.operandoA + self.operandoB
    
aritmetica1 = Aritmetica(7,9)
print(aritmetica1.sumar())