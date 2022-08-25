from Abstracta.Instruccion import Instruccion
from Expresiones.Primitiva import Primitiva


class BreakExpresion(Instruccion):
    def __init__(self, fila, expresion):
        super().__init__(fila)
        self.expresion = expresion
        self.primitiva = None

    def ejecutar(self, entorno):
        expre = self.expresion.ejecutar(entorno)
        if expre:
            tipo = expre.tipo
            valor = expre.valor
            self.primitiva = Primitiva(self.fila, tipo, valor)
            return self
