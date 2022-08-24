from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Enumeradas.OperadorAritmetica import OPERADOR_ARITMETICO
from Enumeradas.OperadorUnario import OPERADOR_UNARIO
from Expresiones.Primitiva import Primitiva
from Abstracta.Instruccion import Instruccion


class Unaria(Instruccion):
    def __init__(self, fila, operador, expresion):
        super().__init__(fila)
        self.operador = operador
        self.expresion = expresion


    def ejecutar(self, entorno: Entorno):
        if self.operador and self.expresion:
            expre = self.expresion.ejecutar(entorno)
            if expre:
                #! para operador unario -
                if self.operador == OPERADOR_UNARIO.MENOS:
                    if expre.tipo == tipoPrimitivo.I64:
                        valor = - expre.valor
                        return Primitiva(self.fila, tipoPrimitivo.I64, valor)

                    if expre.tipo == tipoPrimitivo.F64:
                        valor = - expre.valor
                        return Primitiva(self.fila, tipoPrimitivo.F64, valor)
                #! para operador unario !
                elif self.operador == OPERADOR_UNARIO.NOT:

                    if expre.tipo == tipoPrimitivo.BOOL:
                        valor = not expre.valor
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, valor)
                else:
                    print("Error en unarios")