from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Instrucciones.Break import Break
from Instrucciones.BreakExpresion import BreakExpresion


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
                        # ! --------------PARA EJECUTAR INSTRUCCIOENS------------------
                        for instruccion in self.instrucciones:
                            if (instruccion):  # ! no debe vernir vacio
                                inst = instruccion.ejecutar(nuevo_entorno)  # ! --> Ejecutan una instruccion simple
                                if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                    return inst

                                if isinstance(inst, BreakExpresion):
                                    return inst

                    else:
                        if self.instruc_else:
                            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return,
                                                    entorno.flag_continue)
                            for instruccion in self.instruc_else:
                                if instruccion:
                                    inst = instruccion.ejecutar(nuevo_entorno)
                                    if isinstance(inst, Break) and nuevo_entorno.flag_break:
                                        return inst

                                    if isinstance(inst, BreakExpresion):
                                        return inst
                else:
                    print("La expresion debe de ser de tipo BOOL")
