from Abstracta.Instruccion import Instruccion


class Continue(Instruccion):
    def __init__(self, fila):
        super().__init__(fila)

    def ejecutar(self, entorno):
        return self
