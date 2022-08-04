from Abstracta.Instruccion import Instruccion

class Primitiva(Instruccion):
    def __init__(self, fila, tipo, valor):
        super().__init__(fila)
        self.tipo = tipo
        self.valor = valor

    def ejecutar(self, entorno):
        return self