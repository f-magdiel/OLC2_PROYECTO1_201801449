from Entorno.Funcion import Funcion as ObjetoFuncion
from Entorno.Entorno import Entorno
from Abstracta.Instruccion import Instruccion
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Variable import Variable


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
                            parametro_ref = p_ref.ejecutar(entorno)
                            if (parametro_ref):
                                parametro = funcion.parametros[indice]  # vamos obteniedo uno a uno los valores
                                if (parametro_ref.tipo == parametro.tipo):
                                    valor_arreglo = []
                                    # por si vienen Arreglos........................................
                                    # despues de validar que no sea arreglo se almacena la variable en la lista de parametros
                                    parametros_procesados.append(
                                        Variable(parametro.tipo, parametro.nombre, parametro_ref.valor,self.fila, True))
                                else:
                                    desc = "El tipo ({}) del parametro de llamada no coincide con el tipo ({}) declarado.".format(
                                        parametro_ref.tipo.value, funcion.parametros[indice].tipo.value)
                                    # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                                    print(desc)
                                    todo_correcto = False
                            else:
                                todo_correcto = False
                            indice += 1
                    else:
                        desc = "La cantidad de parametros no coincide con el de la funcion."
                        # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                        print(desc)
                if (todo_correcto):
                    if (funcion.tipo == tipoPrimitivo.NULO):
                        nuevo_entorno = Entorno(entorno, False, False, False)
                    else:
                        nuevo_entorno = Entorno(entorno, False, True, False)
                    if (parametros_procesados):
                        for variable in parametros_procesados:
                            nuevo_entorno.nueva_variable(variable)
                    for instruccion in funcion.instrucciones:
                        if (instruccion):
                            instr = instruccion.ejecutar(nuevo_entorno)
                            # FALTA VALIDAR SI VIENE BREAK O RETURN PARA VALICAION DE RETORNO DE VALORES
            else:
                desc = "No existe una funcion con el nombre '{}' en la tabla de simbolos.".format(self.nombre)
                # lista_errores.append(Error(TIPO_ERROR.SEMANTICO, desc, self.fila))
                print(desc)
