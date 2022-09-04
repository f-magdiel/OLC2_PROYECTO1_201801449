from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Enumeradas.Primitivo import tipoPrimitivo
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class AsignacionVariable(Instruccion):
    def __init__(self, fila, nombre, expresion):
        super().__init__(fila)
        self.nombre = nombre
        self.expresion = expresion

    def ejecutar(self, entorno: Entorno):
        if (self.nombre and self.expresion):
            variable = entorno.buscar_variable(self.nombre)
            if (variable):
                expre = self.expresion.ejecutar(entorno)
                if (expre):
                    if not (isinstance(expre.valor, list)):
                        if (expre.tipo == variable.tipo and expre.tipo != tipoPrimitivo.STRING):  # Si es el mismo tipo
                            nueva_variable = Variable(variable.tipo, variable.nombre, expre.valor, self.fila, variable.mutable)
                            entorno.editar_variable(variable.nombre, nueva_variable)

                        elif ((expre.tipo == tipoPrimitivo.TOS or expre.tipo == tipoPrimitivo.TOW) and variable.tipo == tipoPrimitivo.STRING):  # si es tipo string o str
                            nueva_variable = Variable(variable.tipo, variable.nombre, expre.valor, self.fila, variable.mutable)
                            entorno.editar_variable(variable.nombre, nueva_variable)

                        else:
                            alert = "Error el tipo y la expresion no coinciden"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                else:
                    alert = "Error ocurrió un error al realizar asignación"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error variable no ha sido declarado"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


class AsignacionArreglo(Instruccion):
    def __init__(self, fila, nombre, indices, exp):
        super().__init__(fila)
        self.nombre = nombre
        self.indices = indices
        self.exp = exp

    def ejecutar(self, entorno: Entorno):
        if (self.nombre and self.indices and self.exp):
            variable = entorno.buscar_variable(self.nombre)
            if (variable):
                if (isinstance(variable.valor, list)):
                    posiciones = []
                    errores = []
                    for indice in self.indices:
                        expresion = indice.ejecutar(entorno)
                        if (expresion):
                            if not (isinstance(expresion.valor, list)):
                                if (expresion.valor != None):
                                    if (expresion.tipo == tipoPrimitivo.I64):
                                        if (expresion.valor >= 0):
                                            posiciones.append(expresion.valor)
                                        else:

                                            alert = "Error el indice del arreglo no puede ser un entero negativo"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                            print(alert)
                                    else:

                                        alert = "Error el indice del arreglo no puede ser un valor del tipo ({})".format(expresion.tipo.value)
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                        print(alert)
                                else:

                                    alert = "Error el indice del arreglo no puede ser un valor nulo"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                    print(alert)
                            else:

                                alert = "Error el indice del arreglo no puede ser un arreglo"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)
                        else:
                            alert = "Error al acceder al indice del arreglo"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                            print(alert)

                    if not (errores):

                        arreglo_aux = variable.valor
                        ultimo_arreglo = None
                        ultima_pos = 0
                        valor_arreglo = None
                        try:
                            for pos in posiciones:
                                ultimo_arreglo = arreglo_aux
                                ultima_pos = pos
                                valor_arreglo = arreglo_aux[pos]
                                arreglo_aux = valor_arreglo.valor

                            if not (isinstance(valor_arreglo, list)):

                                expresion = self.exp.ejecutar(entorno)

                                if not (isinstance(expresion.valor, list)):

                                    tipoprimvar = self.obtener_tipo(variable)

                                    if (expresion.tipo == tipoprimvar):
                                        ultimo_arreglo[ultima_pos] = expresion

                                        nueva_variable = Variable(variable.tipo, variable.nombre, variable.valor, self.fila, variable.mutable)

                                        entorno.editar_variable(variable.nombre, nueva_variable)
                                    else:
                                        alert = 'El tipo ({}) y la expresion ({}) de la variable no concuerdan.'.format(variable.tipo.value, expresion.tipo.value)
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                        print(alert)
                                else:
                                    alert = 'No se pueden asignar arreglos.'
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                    print(alert)
                            else:
                                alert = 'No se puede asignar el valor porque en la posicion hay un arreglo.'
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)
                        except:
                            alert = 'El indice supera los limites del arreglo.'
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                            print(alert)
                else:
                    alert = 'La variable con el nombre \'{}\' de tipo ({}) no es un arreglo.'.format(variable.nombre, variable.tipo.value)
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)
            else:
                alert = "No existe una variable con el nombre '{}' en la tabla de simbolos.".format(self.nombre)
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

    def obtener_tipo(self, dato):  # Devuelve el tipo primitivo (si es que hay) del dato arreglo
        if isinstance(dato.valor, list):
            if len(dato.valor) > 0:
                return self.obtener_tipo(dato.valor[0])
        return dato.tipo