from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Instrucciones.BreakExpresion import BreakExpresion

class Loop(Instruccion):
    def __init__(self, fila, listaInstrucciones: list):
        super().__init__(fila)
        self.listaInstrucciones = listaInstrucciones  # ! Lista de instrucciones dentro del loop

    def ejecutar(self, entorno: Entorno):

        if self.listaInstrucciones:
            while True:
                nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                for ele in self.listaInstrucciones:
                    if ele:
                        inst = ele.ejecutar(nuevo_entorno)

                        if isinstance(inst, BreakExpresion):  # * Cuando es un break
                            return inst.primitiva

                        # TODO erororres de return y continue
