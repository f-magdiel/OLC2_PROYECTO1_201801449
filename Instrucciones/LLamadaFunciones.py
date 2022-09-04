from Entorno.Funcion import Funcion as ObjetoFuncion
from Entorno.Entorno import Entorno
from Abstracta.Instruccion import Instruccion
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Variable import Variable
from Instrucciones.Return import Return
from Instrucciones.While import While
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class LlamadaFunciones(Instruccion):
    def __init__(self, fila, nombre, parametros_referencia):
        super().__init__(fila)
        self.nombre = nombre
        self.parametros_referencia = parametros_referencia

    def ejecutar(self, entorno: Entorno):
        if (self.nombre):
            funcion: ObjetoFuncion = entorno.buscar_funcion(self.nombre)
            if (funcion):
                parametros_procesados = []
                todo_correcto = True
                if (len(funcion.parametros) != 0):
                    if (len(funcion.parametros) == len(self.parametros_referencia)):
                        indice = 0
                        for p_ref in self.parametros_referencia:
                            parametro_ref = p_ref[0].ejecutar(entorno)
                            if (parametro_ref):
                                parametro = funcion.parametros[indice]  # vamos obteniedo uno a uno los valores
                                if (parametro_ref.tipo == parametro.tipo):

                                    if (parametro_ref.tipo in [tipoPrimitivo.ARREGLO, tipoPrimitivo.VECTOR]):
                                        if not (p_ref[1]):

                                            alert = "Error no se hizo referencia al valor del arreglo"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                            print(alert)
                                            todo_correcto = False
                                        else:
                                            parametros_procesados.append(Variable(parametro.tipo, parametro.nombre, parametro_ref.valor, self.fila, True))
                                        # despues de validar que no sea arreglo se almacena la variable en la lista de parametros
                                    else:
                                        parametros_procesados.append(Variable(parametro.tipo, parametro.nombre, parametro_ref.valor, self.fila, True))

                                else:

                                    alert = "El tipo del parametro de llamada no coincide con el tipo declarado."
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                    print(alert)
                                    todo_correcto = False
                            else:
                                todo_correcto = False
                            indice += 1
                    else:
                        alert = "Error La cantidad de parametros no coincide con el de la funcion."
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)

                if (todo_correcto):
                    if (funcion.tipo == tipoPrimitivo.NULO):
                        nuevo_entorno = Entorno(entorno, False, False, False)
                        Tabla_Simbolos.append(nuevo_entorno)
                    else:
                        nuevo_entorno = Entorno(entorno, False, True, False)  # ! se manda para retornar en funciones
                        Tabla_Simbolos.append(nuevo_entorno)
                    if (parametros_procesados):
                        for variable in parametros_procesados:
                            nuevo_entorno.nueva_variable(variable)
                    for instruccion in funcion.instrucciones:
                        if (instruccion):

                            instr = instruccion.ejecutar(nuevo_entorno)

                            if (isinstance(instr, Return) and nuevo_entorno.flag_return):

                                if (instr.primitiva.tipo == funcion.tipo):
                                    if not (isinstance(instr.primitiva.valor, list)):
                                        return instr.primitiva
                                    else:
                                        alert = 'Las funciones no pueden retornar arreglos.'
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                        print(alert)
                                else:
                                    alert = 'La funcion de tipo ({}) no puede retornar un valor de tipo ({}).'.format(funcion.tipo.value, instr.primitiva.tipo.value)
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                    print(alert)
                            elif (isinstance(instr, Return) and not nuevo_entorno.flag_return):

                                alert = "La instruccion return solo puede estar dentro de funciones que retonen valores"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)
                    if (funcion.tipo != tipoPrimitivo.NULO):
                        alert = "Error La funcion es de tipo ({}) con lo cual, debe retornar un valor".format(funcion.tipo.value)
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)
            else:

                alert = "Error no existe una funcion con el nombre '{}' en la tabla de simbolos".format(self.nombre)
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

        else:
            alert = "Error con el nombre de la funcion llamada"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
