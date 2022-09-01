from Abstracta.Instruccion import Instruccion
from Entorno.Variable import Variable
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Enumeradas.NativeVectores import NATIVE_VECTORES
from Enumeradas.Primitivo import tipoPrimitivo


class NativasVectores(Instruccion):
    def __init__(self, fila, expresion1, funcion, expresion2=None):
        super().__init__(fila)
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.funcion = funcion

    def ejecutar(self, entorno: Entorno):

        if NATIVE_VECTORES.LEN == self.funcion:
            # ! Busco el nombre = id
            var = self.expresion1.ejecutar(entorno)
            tam = len(var.valor)
            return Primitiva(self.fila, tipoPrimitivo.I64, tam)
        elif NATIVE_VECTORES.CAPACITY == self.funcion:
            pass
        elif NATIVE_VECTORES.PUSH == self.funcion:
            pass
        elif NATIVE_VECTORES.CONTAINS == self.funcion:
            pass
        elif NATIVE_VECTORES.REMOVE == self.funcion:
            pass
        elif NATIVE_VECTORES.INSERT == self.funcion:
            pass
        else:
            pass
            # ! Errores
