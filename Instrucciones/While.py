from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
from Instrucciones.BreakExpresion import BreakExpresion
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class While(Instruccion):
    def __init__(self, fila, expresion, instrucciones: list):
        super().__init__(fila)
        self.expresion = expresion
        self.instrucciones = instrucciones

    def ejecutar(self, entorno: Entorno):
        if self.expresion and self.instrucciones:
            nuevo_entorno = Entorno(entorno, True, entorno.flag_return, True)
            Tabla_Simbolos.append(nuevo_entorno)
            while (self.evaluar_expresion(self.expresion, entorno)):

                for inst in self.instrucciones:
                    if inst:
                        instruc = inst.ejecutar(nuevo_entorno)

                        if isinstance(instruc, Break) and nuevo_entorno.flag_break:  # * Cuando es un break
                            return None

                        if isinstance(instruc, BreakExpresion) and nuevo_entorno.flag_break:
                            alert = "Error el Break expresion solo debe estar en el loop"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                            return

                        if isinstance(instruc, Continue) and nuevo_entorno.flag_continue:
                            break

                        if isinstance(instruc, Return) and nuevo_entorno.flag_return:
                            return instruc
                        elif isinstance(instruc, Return) and not nuevo_entorno.flag_return:
                            alert = "Error el Return solo debe estar en funciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                            return

                    else:
                        alert = "Error de instrucciones en while"
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


    def evaluar_expresion(self, expres, entorno: Entorno):
        cond = expres.ejecutar(entorno)
        if cond:
            if cond.tipo == tipoPrimitivo.BOOL:
                return cond.valor
        else:
            alert = "Error evaluar expresion en while"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
