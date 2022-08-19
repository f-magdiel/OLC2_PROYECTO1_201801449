from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno


class ElseIf(Instruccion):
    def __init__(self, fila, expresion, instrucciones: list, elseif: list, instelse: list):
        super().__init__(fila)
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.elseif = elseif
        self.instelse = instelse

    def ejecutar(self, entorno):
        if self.expresion:
            expre = self.expresion.ejecutar(entorno)
            if expre:
                if expre.tipo == tipoPrimitivo.BOOL:
                    if expre.valor:
                        nuevo_entorno = Entorno(entorno, None)
                        for instruccion in self.instrucciones:
                            if instruccion:
                                inst = instruccion.ejecutar(nuevo_entorno)

                    else:
                        cumple = False
                        for else_if in self.elseif:
                            expre = else_if[0].ejecutar(entorno)
                            if expre:
                                if expre.tipo == tipoPrimitivo.BOOL:
                                    if expre.valor:
                                        cumple = True
                                        nuevo_entorno = Entorno(entorno, None)
                                        for instruc in else_if[1]:
                                            if instruc:
                                                inst = instruc.ejecutar(nuevo_entorno)
                                        break

                        if not cumple:
                            if self.instelse:
                                nuevo_entorno = Entorno(entorno, None)
                                for instruccion in self.instelse:
                                    if instruccion:
                                        inst = instruccion.ejecutar(nuevo_entorno)
