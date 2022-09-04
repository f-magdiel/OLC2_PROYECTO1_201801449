from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Instrucciones.Break import Break
from Instrucciones.BreakExpresion import BreakExpresion
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class If(Instruccion):
    def __init__(self, fila, expresion, instrucciones: list, instruc_else: list):
        super().__init__(fila)
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.instruc_else = instruc_else

    def ejecutar(self, entorno: Entorno):
        if self.expresion and self.instrucciones:  # ! Que no vengan vacios
            expre = self.expresion.ejecutar(entorno)
            if expre:
                if expre.tipo == tipoPrimitivo.BOOL:
                    if expre.valor:
                        nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                        Tabla_Simbolos.append(nuevo_entorno)
                        # ! --------------PARA EJECUTAR INSTRUCCIOENS------------------
                        for instruccion in self.instrucciones:

                            if (instruccion):  # ! no debe vernir vacio
                                inst = instruccion.ejecutar(nuevo_entorno)  # ! --> Ejecutan una instruccion simple

                                if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                    return inst
                                elif isinstance(inst, Break) and nuevo_entorno.flag_break:
                                    alert = "Error el Break solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if isinstance(inst, BreakExpresion):
                                    return inst
                                elif isinstance(inst, BreakExpresion) and not nuevo_entorno.flag_break:
                                    alert = "Error el Break solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                    return inst
                                elif isinstance(inst, Continue) and not nuevo_entorno.flag_continue:
                                    alert = "Error el Continue solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if isinstance(inst, Return) and nuevo_entorno.flag_return:
                                    return inst
                                elif isinstance(inst, Return) and not nuevo_entorno.flag_return:
                                    alert = "Error el Retunr solo puede estar dentro de ciclos"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                            else:
                                alert = "Error al ejecutar instrucciones"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    else:
                        if self.instruc_else:
                            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return,entorno.flag_continue)
                            Tabla_Simbolos.append(nuevo_entorno)
                            for instruccion in self.instruc_else:
                                if instruccion:
                                    inst = instruccion.ejecutar(nuevo_entorno)
                                    #! Break
                                    if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                        return inst
                                    elif isinstance(inst, Break) and not nuevo_entorno.flag_break:
                                        alert = "Error el Break solo puede estar dentro de ciclos"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                    #! Break expresion
                                    if isinstance(inst, BreakExpresion) and nuevo_entorno.flag_break:
                                        return inst
                                    elif isinstance(inst, BreakExpresion) and not nuevo_entorno.flag_break:
                                        alert = "Error el Break solo puede estar dentro de ciclos"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                    #! Continue
                                    if isinstance(inst, Continue) and nuevo_entorno.flag_continue:
                                        return inst
                                    elif isinstance(inst, Continue) and not nuevo_entorno.flag_continue:
                                        alert = "Error el Continue solo puede estar dentro de ciclos"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                    #! Return
                                    if isinstance(inst, Return) and nuevo_entorno.flag_return:
                                        return inst
                                    elif isinstance(inst, Return) and not nuevo_entorno.flag_return:
                                        alert = "Error el Retunr solo puede estar dentro de ciclos"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                else:
                                    alert = "Error al ejecutar instrucciones"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                else:
                    alert = "La expresion debe ser de tipo BOOL"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error al ejecutar expresion"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

        else:
            alert = "Error al ingresar a la validacion"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
