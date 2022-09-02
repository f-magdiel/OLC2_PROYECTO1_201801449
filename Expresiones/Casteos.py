from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Expresiones.Primitiva import Primitiva


class Casteos(Instruccion):
    def __init__(self, fila, expresion, tipo):
        super().__init__(fila)
        self.expresion = expresion
        self.tipo = tipo

    def ejecutar(self, entorno):
        data = self.expresion.ejecutar(entorno)

        if data:
            # ! I64
            if self.tipo == tipoPrimitivo.I64:
                if data.tipo in [tipoPrimitivo.I64, tipoPrimitivo.F64, tipoPrimitivo.BOOL, tipoPrimitivo.CHAR]:
                    # si es char
                    if data.tipo == tipoPrimitivo.CHAR:
                        val = ord(data.valor)
                    else:
                        val = int(data.valor)

                    return Primitiva(self.fila, tipoPrimitivo.I64, val)
                else:
                    pass
            # ! F64
            elif self.tipo == tipoPrimitivo.F64:
                if data.tipo in [tipoPrimitivo.I64, tipoPrimitivo.F64]:
                    val = float(data.valor)
                    return Primitiva(self.fila, tipoPrimitivo.F64, val)
                else:
                    pass
            # ! BOOL
            elif self.tipo == tipoPrimitivo.BOOL:
                if data.tipo == tipoPrimitivo.BOOL:
                    val = data.valor
                    return Primitiva(self.fila, tipoPrimitivo.BOOL, val)
                else:
                    pass
            # ! CHAR
            elif self.tipo == tipoPrimitivo.CHAR:
                if data.tipo in [tipoPrimitivo.I64, tipoPrimitivo.CHAR]:
                    if int(data.valor) >= 0:
                        val = chr(data.valor)
                        return Primitiva(self.fila, tipoPrimitivo.CHAR, val)
                    else:
                        pass
                else:
                    pass
            # ! STR
            elif self.tipo == tipoPrimitivo.STR:
                if data.tipo == tipoPrimitivo.STR:
                    val = data.valor
                    return Primitiva(self.fila, tipoPrimitivo.STR, val)

            # ! STRING
            elif self.tipo == tipoPrimitivo.STRING:
                if data.tipo == tipoPrimitivo.STRING:
                    val = data.valor
                    return Primitiva(self.fila, tipoPrimitivo.STRING, val)
                else:
                    pass

        else:
            pass
