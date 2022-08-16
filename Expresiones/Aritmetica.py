from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.OperadorAritmetica import OPERADOR_ARITMETICO
from Enumeradas.Primitivo import tipoPrimitivo
from Expresiones.Primitva import Primitiva


class Aritmetica(Instruccion):
    def __init__(self, fila, exp1, operador, exp2):
        super().__init__(fila)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador


    def ejecutar(self, entorno: Entorno):
        if self.exp1 and self.exp2 and self.operador: #! Que no venga vacío
            expresion1 = self.exp1.ejecutar(entorno)
            expresion2 = self.exp2.ejecutar(entorno)

            if expresion1 and expresion2:
                if not (isinstance(expresion1.valor, list) or isinstance(expresion2.valor, list)):
                    #! Operacion SUMA
                    if self.operador == OPERADOR_ARITMETICO.MAS:
                        if expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:#! suma de float
                            resultado = float(expresion1.valor) + float(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.F64, resultado)

                        elif expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64: #! Suma de enteros
                            resultado = int(expresion1.valor) + int(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.I64, resultado)

                        elif expresion1.tipo == tipoPrimitivo.STR and (expresion2.tipo == tipoPrimitivo.TOS or expresion2.tipo == tipoPrimitivo.TOW): #! para concatenar string
                            resultado = str(expresion1.valor) + str(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.STR, resultado)



