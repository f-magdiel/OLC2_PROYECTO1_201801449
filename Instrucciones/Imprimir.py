from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Variable, Entorno


class Imprimir(Instruccion):
    def __init__(self, fila, expresion, expresiones: list):
        self.fila = fila
        self.expresion = expresion
        self.expresiones = expresiones

    def ejecutar(self,entorno: Entorno):
        print("Expresion {}".format(self.expresion))
        print("Expresiones {}".format(self.expresiones))
