from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno

class MainInstru(Instruccion):
    def __init__(self, fila, instruccines):
        super().__init__(fila)
        self.instrucciones = instruccines

    def ejecutar(self, entorno: Entorno):
        if self.instrucciones:
            for instruccion in self.instrucciones:
                instruccion.ejecutar(entorno)
                # TODO validar eso