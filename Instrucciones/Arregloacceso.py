from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Expresiones.Primitiva import Primitiva
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class Arregloacceso(Instruccion):
    def __init__(self, fila, nombre, indices):
        super().__init__(fila)
        self.nombre = nombre
        self.indices = indices

    def ejecutar(self, entorno: Entorno):
        if (self.nombre and self.indices):
            variable = entorno.buscar_variable(self.nombre)

            if (variable):
                if (isinstance(variable.valor, list)):
                    posiciones = []

                    for indice in self.indices:

                        expresion = indice.ejecutar(entorno)

                        if (expresion):

                            if not (isinstance(expresion.valor, list)):

                                if (expresion.valor != None):

                                    if (expresion.tipo == tipoPrimitivo.I64):

                                        if (expresion.valor >= 0):
                                            posiciones.append(expresion.valor)
                                            # print("valor de posicion: ",expresion.valor)
                                        else:
                                            alert = 'El indice del arreglo no puede ser un entero negativo.'
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                            print(alert)
                                            return None
                                    else:
                                        alert = 'El indice del arreglo no puede ser un valor de tipo ({}).'.format(expresion.tipo.value)
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                        print(alert)
                                        return None
                                else:
                                    alert = 'El indice del arreglo no puede ser un valor nulo.'
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                    print(alert)
                                    return None
                            else:
                                alert = 'El indice del arreglo no puede ser un arreglo.'
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)
                                return None
                        else:
                            return None
                    arreglo_aux = variable.valor
                    # print(arreglo_aux)
                    valor_arreglo = None
                    try:

                        for pos in posiciones:
                            valor_arreglo = arreglo_aux[pos]
                            arreglo_aux = valor_arreglo.valor

                        return Primitiva(self.fila, valor_arreglo.tipo, valor_arreglo.valor)
                    except:
                        alert = 'El indice supera los limites del arreglo.'
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)
                else:
                    alert = 'La variable con el nombre \'{}\' de tipo ({}) no es un arreglo.'.format(variable.nombre, variable.tipo.value)
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)
            else:
                alert = 'No existe una variable con el nombre \'{}\' en la tabla de simbolos.'.format(self.nombre)
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)
