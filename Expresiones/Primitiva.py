from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno


class Primitiva(Instruccion):
    def __init__(self, fila, tipo, valor, capacidad=None):
        super().__init__(fila)
        self.tipo = tipo
        self.valor = valor
        self.capacidad = capacidad

    def ejecutar(self, entorno: Entorno):
        return self
