from Abstracta.Instruccion import Instruccion
from Expresiones.Primitva import Primitiva
from Entorno.Entorno import Entorno
from Enumeradas.OperadorRelacional import OPERADOR_RELACIONAL
from Enumeradas.Primitivo import tipoPrimitivo

class Relacional(Instruccion):
    def __init__(self, fila, expresion1, operador, expresion2):
        super().__init__(fila)
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.operador = operador

    def ejecutar(self, entorno:Entorno):
        if self.expresion1 and self.expresion2 and self.operador:
            expre1 = self.expresion1.ejecutar(entorno)
            expre2 = self.expresion2.ejecutar(entorno)
            if expre1 and expre2:
                #! Igualacion ==
                if self.operador == OPERADOR_RELACIONAL.IGUALQUE:
                    #! para entero
                    if expre1.tipo == tipoPrimitivo.I64 and expre2.tipo == tipoPrimitivo.I64:
                        resultado = int(expre1.valor) == int(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    #! para float
                    elif expre1.tipo == tipoPrimitivo.F64 and expre2.tipo == tipoPrimitivo.F64:
                        resultado = float(expre1.valor) == float(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    #! Para string
                    elif expre1.tipo == tipoPrimitivo.STR and expre2.tipo == tipoPrimitivo.STR:
                        resultado = str(expre1.valor) == str(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    else:
                        print("Error de igualacion")
                #! Mayor que >
                elif self.operador == OPERADOR_RELACIONAL.MAYORQUE:
                    #! para entero
                    if expre1.tipo == tipoPrimitivo.I64 and expre2.tipo == tipoPrimitivo.I64:
                        resultado = int(expre1.valor) > int(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    #! para float
                    elif expre1.tipo == tipoPrimitivo.F64 and expre2.tipo == tipoPrimitivo.F64:
                        resultado = float(expre1.valor) > float(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    #! para string
                    elif expre1.tipo == tipoPrimitivo.STR and expre2.tipo == tipoPrimitivo.STR:
                        resultado = str(expre1.valor) > str(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    else:
                        print("Error de mayor que")
                #! Menor que <
                elif self.operador == OPERADOR_RELACIONAL.MENORQUE:
                    # ! para entero
                    if expre1.tipo == tipoPrimitivo.I64 and expre2.tipo == tipoPrimitivo.I64:
                        resultado = int(expre1.valor) < int(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    # ! para float
                    elif expre1.tipo == tipoPrimitivo.F64 and expre2.tipo == tipoPrimitivo.F64:
                        resultado = float(expre1.valor) < float(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    # ! para string
                    elif expre1.tipo == tipoPrimitivo.STR and expre2.tipo == tipoPrimitivo.STR:
                        resultado = str(expre1.valor) < str(expre2.valor)
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    else:
                        print("Error de menor que")

