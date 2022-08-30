from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Expresiones.Primitiva import Primitiva


class Arregloacceso(Instruccion):
    def __init__(self, fila, nombre, indices):
        super().__init__(fila)
        self.nombre = nombre
        self.indices = indices

    def ejecutar(self, entorno: Entorno):
        if (self.nombre and self.indices):
            variable: Variable = entorno.buscar_variable(self.nombre)
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
                                            desc = 'El indice del arreglo no puede ser un entero negativo.'
                                            # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                                            print(desc)
                                            return None
                                    else:
                                        desc = 'El indice del arreglo no puede ser un valor de tipo ({}).'.format(expresion.tipo.value)
                                        # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                                        print(desc)
                                        return None
                                else:
                                    desc = 'El indice del arreglo no puede ser un valor nulo.'
                                    # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                                    print(desc)
                                    return None
                            else:
                                desc = 'El indice del arreglo no puede ser un arreglo.'
                                # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                                print(desc)
                                return None
                        else:
                            return None
                    arreglo_aux = variable.valor
                    # print(arreglo_aux)
                    valor_arreglo = None
                    try:

                        for pos in posiciones:
                            valor_arreglo = arreglo_aux[pos]
                            # print(valor_arreglo)
                            arreglo_aux = valor_arreglo.valor

                        return Primitiva(self.fila, valor_arreglo.tipo, valor_arreglo.valor)
                    except:
                        desc = 'El indice supera los limites del arreglo.'
                        # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                        print(desc)
                else:
                    desc = 'La variable con el nombre \'{}\' de tipo ({}) no es un arreglo.'.format(variable.nombre, variable.tipo.value)
                    # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                    print(desc)
            else:
                desc = 'No existe una variable con el nombre \'{}\' en la tabla de simbolos.'.format(self.nombre)
                # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                print(desc)
