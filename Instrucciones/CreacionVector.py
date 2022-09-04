from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Enumeradas.Primitivo import tipoPrimitivo
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class CreacionVector(Instruccion):
    def __init__(self, fila, expresion=None):
        super().__init__(fila)
        self.expresion = expresion


    def ejecutar(self, entorno: Entorno):

        if self.expresion is None:
            return Primitiva(self.fila, tipoPrimitivo.VECTOR, [])
        else:
            data = self.expresion.ejecutar(entorno)
            #print("data",data.valor)
            if data:
                tipo = data.tipo

                if tipo == tipoPrimitivo.I64:
                    valor = data.valor
                    if valor > 0:
                        return Primitiva(self.fila, tipoPrimitivo.VECTOR, [], valor)
                    else:
                        alert = "Error valor es invalido en vector"
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)
                else:
                    alert = "Error el tipo de datos es incorrecto en vector"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)
            else:
                alert = "Error al ejecutar expresion de vector"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)
