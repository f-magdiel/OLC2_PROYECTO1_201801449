from Abstracta.Instruccion import Instruccion
from Expresiones.Primitiva import Primitiva
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class BreakExpresion(Instruccion):
    def __init__(self, fila, expresion):
        super().__init__(fila)
        self.expresion = expresion
        self.primitiva = None

    def ejecutar(self, entorno):
        expre = self.expresion.ejecutar(entorno)
        if expre:
            tipo = expre.tipo
            valor = expre.valor
            self.primitiva = Primitiva(self.fila, tipo, valor)
            return self
        else:
            alert = "Error el ejecutar Break expresion "
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
