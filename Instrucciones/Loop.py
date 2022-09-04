from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Instrucciones.BreakExpresion import BreakExpresion
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class Loop(Instruccion):
    def __init__(self, fila, listaInstrucciones: list):
        super().__init__(fila)
        self.listaInstrucciones = listaInstrucciones  # ! Lista de instrucciones dentro del loop

    def ejecutar(self, entorno: Entorno):

        if self.listaInstrucciones:
            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
            Tabla_Simbolos.append(nuevo_entorno)
            while True:

                for ele in self.listaInstrucciones:

                    inst = ele.ejecutar(nuevo_entorno)
                    if inst:
                        if isinstance(inst, BreakExpresion):  # * Cuando es un break
                            return inst.primitiva

        else:
            alert = "Error el ejecutar el loop"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

