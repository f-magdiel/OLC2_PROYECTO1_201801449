from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class Return(Instruccion):
    def __init__(self, fila, exp):
        super().__init__(fila)
        self.exp = exp
        self.primitiva = None

    def ejecutar(self, entorno: Entorno):
        expre = self.exp.ejecutar(entorno)
        if (expre):
            tipo = expre.tipo
            valor = expre.valor
            self.primitiva = Primitiva(self.fila, tipo, valor)
            return self
        else:
            alert = "Error al ejecutar Return"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
