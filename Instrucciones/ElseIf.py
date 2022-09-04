from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Instrucciones.Break import Break
from Instrucciones.BreakExpresion import BreakExpresion
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


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
                        Tabla_Simbolos.append(nuevo_entorno)
                        for instruccion in self.instrucciones:
                            if instruccion:
                                inst = instruccion.ejecutar(nuevo_entorno)
                                if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                    return inst
                                elif isinstance(inst, Break) and not nuevo_entorno.flag_break:
                                    alert = "Error el Break solo puede estar dentro de ciclos "
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if isinstance(inst, BreakExpresion) and nuevo_entorno.flag_break:
                                    return inst
                                elif isinstance(inst, BreakExpresion) and not nuevo_entorno.flag_break:
                                    alert = "Error el Break expresion solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                    return inst
                                elif isinstance(inst,Continue) and not nuevo_entorno.flag_continue:
                                    alert = "Error el Continue solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if isinstance(inst, Return) and nuevo_entorno.flag_return:
                                    return inst
                                elif isinstance(inst,Return) and not nuevo_entorno.flag_return:
                                    alert = "Error el Retunr solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                            else:
                                alert = "Error al ejecutar instrucciones"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    else:
                        cumple = False
                        for else_if in self.elseif:
                            expre = else_if[0].ejecutar(entorno)
                            if expre:
                                if expre.tipo == tipoPrimitivo.BOOL:
                                    if expre.valor:
                                        cumple = True
                                        nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                        Tabla_Simbolos.append(nuevo_entorno)
                                        for instruc in else_if[1]:
                                            if instruc:
                                                inst = instruc.ejecutar(nuevo_entorno)
                                                if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                                    return inst
                                                elif isinstance(inst, Break) and not nuevo_entorno.flag_break:
                                                    alert = "Error el Break solo puede estar dentro de ciclos"
                                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                                if isinstance(inst, BreakExpresion) and nuevo_entorno.flag_break:
                                                    return inst
                                                elif isinstance(inst, BreakExpresion) and not nuevo_entorno.flag_break:
                                                    alert = "Error el Break expresion solo puede estar dentro de ciclos"
                                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                                if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                                    return inst
                                                elif isinstance(inst, Continue) and not nuevo_entorno.flag_continue:
                                                    alert = "Error el Continue solo puede estar dentro de ciclos"
                                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                                if isinstance(inst, Return) and nuevo_entorno.flag_return:
                                                    return inst
                                                elif isinstance(inst, Return) and not nuevo_entorno.flag_return:
                                                    alert = "Error el Return solo puede estar dentro de ciclos"
                                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                            else:
                                                alert = "Error al ejecutar instrucciones"
                                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                        break

                        if not cumple:
                            if self.instelse:
                                nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                Tabla_Simbolos.append(nuevo_entorno)
                                for instruccion in self.instelse:
                                    if instruccion:
                                        inst = instruccion.ejecutar(nuevo_entorno)
                                        if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                            return inst
                                        elif isinstance(inst, Break) and not nuevo_entorno.flag_break:
                                            alert = "Error el Break solo puede estar dentro de ciclos"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                        if isinstance(inst, BreakExpresion) and nuevo_entorno.flag_break:
                                            return inst
                                        elif isinstance(inst, BreakExpresion) and not nuevo_entorno.flag_break:
                                            alert = "Error el Break expresion solo puede estar dentro de ciclos"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                        if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                            return inst
                                        elif isinstance(inst, Continue) and not nuevo_entorno.flag_continue:
                                            alert = "Error el Continue solo puede estar dentro de ciclos"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                        if isinstance(inst, Return) and nuevo_entorno.flag_return:
                                            return inst
                                        elif isinstance(inst,Return) and not nuevo_entorno.flag_return:
                                            alert = "Error el Return solo puede estar dentro de ciclos"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                    else:
                                        alert = "Error al ejecutar instrucciones"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                else:
                    alert = "Error el tipo es incompatible"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error el ejecutar la expresion"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

        else:
            alert = "Error la expresion viene vacio"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
