from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno


class Loop(Instruccion):
    def __init__(self, fila, listaInstrucciones: list):
        super().__init__(fila)
        self.listaInstrucciones = listaInstrucciones  # !Lista de instrucciones dentro del loop

    def ejecutar(self, entorno: Entorno):
        if self.listaInstrucciones:
            while True:
                nuevo_entorno = Entorno(entorno,None)
                for ele in self.listaInstrucciones:
                    ele.ejecutar(nuevo_entorno)
