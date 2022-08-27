from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva


class Return(Instruccion):
    def __init__(self, fila, exp):
        super().__init__(fila)
        self.exp = exp
        self.primitiva = None

    def ejecutar(self, entorno: Entorno):
        expre = self.exp.ejecutar(entorno)
        if (expre):
            tipo = expre.tipo
            valor = expre.valor
            self.primitiva = Primitiva(self.fila, tipo, valor)
            return self
