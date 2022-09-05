from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Variable import Variable
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class DeclaracionVector(Instruccion):
    def __init__(self, fila, id, expresion, tipo, mutable):
        super().__init__(fila)
        self.id = id
        self.expresion = expresion
        self.tipo = tipo
        self.mutable = mutable

    def ejecutar(self, entorno: Entorno):
        data = self.expresion.ejecutar(entorno)

        if data:
            if data.tipo == tipoPrimitivo.VECTOR:
                # ! recorrer arreglo
                iguales = True
                for i in range(len(data.valor)):
                    if data.valor[i].tipo != self.tipo:
                        iguales = False
                        break


                # validar
                if iguales:
                    # print(self.id)
                    variable = Variable(tipoPrimitivo.VECTOR, self.id, data.valor, self.fila, self.mutable, data.capacidad)
                    entorno.nueva_variable(variable)
                else:
                    alert = "Error el tipo de datos es incorrecto en expresion de arreglo"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)
            else:
                alert = "Error la expresion no es de tipo vector"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)
        else:
            alert = "Error la capacidad asignada al vector es inválida"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
