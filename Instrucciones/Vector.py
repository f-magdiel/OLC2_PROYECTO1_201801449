from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Expresiones.Primitiva import Primitiva
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class Vector(Instruccion):
    def __init__(self, fila, arreglo):
        super().__init__(fila)
        self.arreglo = arreglo

    def ejecutar(self, entorno: Entorno):
        data = self.arreglo.ejecutar(entorno)
        if data:
            return Primitiva(self.fila, tipoPrimitivo.VECTOR, data.valor)
        else:
            alert = "Error al ejecutar el vector "
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
