import copy
import math

from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Nativas import NATIVAS
from Enumeradas.Primitivo import tipoPrimitivo
from Expresiones.Primitiva import Primitiva


class FuncionesNativas(Instruccion):
    def __init__(self, fila, funcion, expresion):
        super().__init__(fila)
        self.funcion = funcion
        self.expresion = expresion

    def ejecutar(self, entorno):
        data = self.expresion.ejecutar(entorno)
        if data:
            tipo_data = data.tipo
            # ! ABSOLUTO
            if self.funcion == NATIVAS.ABS:
                # ! I64
                if tipo_data == tipoPrimitivo.I64:
                    val = abs(data.valor)
                    return Primitiva(self.fila, tipoPrimitivo.I64, val)
                # ! F64
                elif tipo_data == tipoPrimitivo.F64:
                    val = abs(data.valor)
                    return Primitiva(self.fila, tipoPrimitivo.F64, val)
                else:
                    pass
            # ! RAIZ
            elif self.funcion == NATIVAS.SQRT:
                # ! I64 & F64
                if tipo_data in [tipoPrimitivo.I64, tipoPrimitivo.F64]:
                    if data.valor >= 0:
                        val = math.sqrt(data.valor)
                        return Primitiva(self.fila, tipoPrimitivo.F64, val)
                    else:
                        pass
                else:
                    pass
            # ! CLONE
            elif self.funcion == NATIVAS.CLONE:
                val = copy.deepcopy(data.valor)
                return Primitiva(self.fila, tipo_data, val)

            # ! ERRROR DE NATIVAS
            else:
                return Primitiva(self.fila, tipoPrimitivo.TOS, data.valor)
