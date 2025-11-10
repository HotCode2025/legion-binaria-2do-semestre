class FiguraGeometrica:
   
    def __init__(self, alto, ancho):
        if self._validar_valores(alto):
            self._alto = alto
        else: 
            self._alto = 0
            print(f"Valor de alto no válido {ancho}")
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor de ancho no válido {ancho}")


    @property
    def alto(self):
        return self._alto

    @property
    def ancho(self):
        return self._ancho
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')
        
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')
        
    def __str__(self):
        return f"FiguraGeometrica: [Alto: {self._alto}, Ancho: {self._ancho}]"
    
    def _validar_valores(self, valor): #Método encapsulado
        return True if 0 < valor < 10 else False