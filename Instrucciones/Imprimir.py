from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno

listimpresion = []


class Imprimir(Instruccion):
    def __init__(self, fila, expresion, expresiones: list):
        super().__init__(fila)
        self.expresion = expresion
        self.expresiones = expresiones

    def ejecutar(self, entorno: Entorno):
        if self.expresion is not None and self.expresiones is not None :
            expre = self.expresion.ejecutar(entorno)
            list_expre = str(expre.valor).split()
            count_sep = list_expre.count("{}")
            if count_sep == len(self.expresiones): #validar que tenga los mismos {} y parametros
                #ejecutar


        elif self.expresion:
            expre = self.expresion.ejecutar(entorno)
            if expre:
                if isinstance(expre.valor, str):
                    val = str(expre.valor).split(sep="\n")
                    for i in val:
                        listimpresion.append(i)
                else:
                    listimpresion.append(expre.valor.valor)