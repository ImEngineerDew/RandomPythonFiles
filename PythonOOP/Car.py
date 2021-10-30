class Car:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'Detenido'
        self._motor = Motor(cilindros=4)
    
    def arranca(self,tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyectaGasolina(10)
        else:
            self._motor.inyectaGasolina(3)
        

class Motor:
    def __init__(self,cilindros,tipo='gasolina')
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyectaGasolina(self,cantidad):
        pass