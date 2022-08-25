from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Instrucciones.Break import Break
from Instrucciones.BreakExpresion import BreakExpresion
from Instrucciones.Continue import Continue

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
                        nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                        for instruccion in self.instrucciones:
                            if instruccion:
                                inst = instruccion.ejecutar(nuevo_entorno)
                                if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                    return inst

                                if isinstance(inst, BreakExpresion):
                                    return inst

                                if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                    return inst

                    else:
                        cumple = False
                        for else_if in self.elseif:
                            expre = else_if[0].ejecutar(entorno)
                            if expre:
                                if expre.tipo == tipoPrimitivo.BOOL:
                                    if expre.valor:
                                        cumple = True
                                        nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                        for instruc in else_if[1]:
                                            if instruc:
                                                inst = instruc.ejecutar(nuevo_entorno)
                                                if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                                    return inst

                                                if isinstance(inst, BreakExpresion):
                                                    return inst

                                                if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                                    return inst
                                        break

                        if not cumple:
                            if self.instelse:
                                nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                for instruccion in self.instelse:
                                    if instruccion:
                                        inst = instruccion.ejecutar(nuevo_entorno)
                                        if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                            return inst

                                        if isinstance(inst, BreakExpresion):
                                            return inst

                                        if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                            return inst
