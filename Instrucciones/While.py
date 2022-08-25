from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Break import Break

class While(Instruccion):
    def __init__(self, fila, expresion, instrucciones: list):
        super().__init__(fila)
        self.expresion = expresion
        self.instrucciones = instrucciones

    def ejecutar(self, entorno: Entorno):
        if self.expresion and self.instrucciones:
            while (self.evaluar_expresion(self.expresion, entorno)):
                nuevo_entorno = Entorno(entorno, True, entorno.flag_return, entorno.flag_continue)
                for inst in self.instrucciones:
                    if inst:
                        instruc = inst.ejecutar(nuevo_entorno)
                        if isinstance(instruc, Break):# * Cuando es un break
                            return None

                        # TODO erorres break expresion y retunr



    def evaluar_expresion(self, expres, entorno: Entorno):
        cond = expres.ejecutar(entorno)
        if cond:
            if cond.tipo == tipoPrimitivo.BOOL:
                return cond.valor
