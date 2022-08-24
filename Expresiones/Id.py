from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Expresiones.Primitiva import Primitiva


class Id(Instruccion):
    def __init__(self, fila, nombre):
        super().__init__(fila)
        self.nombre = nombre

    def ejecutar(self, entorno: Entorno):
        if (self.nombre):
            variable: Variable = entorno.buscar_variable(self.nombre)
            if (variable):
                tipo = variable.tipo
                valor = variable.valor
                return Primitiva(self.fila, tipo, valor)
            else:
                print("No existe variable")
