from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Enumeradas.OperadorLogico import OPERADOR_LOGICO
from Expresiones.Primitva import Primitiva
from Entorno.Entorno import Entorno


class Logica(Instruccion):
    def __init__(self, fila, expresion1, operador, expresion2):
        super().__init__(fila)
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.operador = operador

    def ejecutar(self, entorno: Entorno):
        if self.expresion1 and self.expresion2 and self.operador:
            expre1 = self.expresion1.ejecutar(entorno)
            expre2 = self.expresion2.ejecutar(entorno)
            if expre1 and expre2:
                if expre1.tipo == tipoPrimitivo.BOOL and expre2.tipo == tipoPrimitivo.BOOL:
                    # ! para or
                    if self.operador == OPERADOR_LOGICO.OR:
                        resultado = expre1.valor or expre2.valor
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    # ! para and
                    elif self.operador == OPERADOR_LOGICO.AND:
                        resultado = expre1.valor and expre2.valor
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)