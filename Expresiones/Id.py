from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Expresiones.Primitiva import Primitiva
from Enumeradas.Primitivo import tipoPrimitivo
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

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
                alert = "Error ({}) no ha sido declarado".format(self.nombre)
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

