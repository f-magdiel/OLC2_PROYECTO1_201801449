from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno


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
                        nuevo_entorno = Entorno(entorno, None)
                        #! --------------PARA EJECUTAR INSTRUCCIOENS------------------
                        for instruccion in self.instrucciones:
                            if(instruccion): #! no debe vernir vacio
                                inst = instruccion.ejecutar(nuevo_entorno) #! --> Ejecutan una instruccion simple

                    else:
                        if self.instruc_else:
                            nuevo_entorno = Entorno(entorno, None)
                            for instruccion in self.instruc_else:
                                if instruccion:
                                    inst = instruccion.ejecutar(nuevo_entorno)
                else:
                    print("La expresion debe de ser de tipo BOOL")
