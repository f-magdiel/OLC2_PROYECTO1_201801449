import Expresiones
from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Entorno.Variable import Variable
from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class ForIn(Instruccion):
    def __init__(self, fila, id, exp1, instrucciones, exp2=None):
        super().__init__(fila)
        self.id = id
        self.exp1 = exp1
        self.exp2 = exp2
        self.instrucciones = instrucciones

    def ejecutar(self, entorno: Entorno):
        data1 = self.exp1.ejecutar(entorno)
        if data1:
            # ! obtener de un el tipo
            type1 = data1.tipo
            arreglo = []
            tipin = None
            # ! validar si viene expre2
            if self.exp2:
                data2 = self.exp2.ejecutar(entorno)

                if data2:
                    type2 = data2.tipo

                    # ! ambos tienen que ser de tipo i64
                    if type1 == tipoPrimitivo.I64 and type2 == tipoPrimitivo.I64:
                        # ! proceso del ciclo for
                        if data2.valor > data1.valor:  # ! validar que expre2 sea mayor que expre1
                            for val in range(data1.valor, data2.valor):
                                arreglo.append(Primitiva(self.fila, tipoPrimitivo.I64, val))

                            tipin = tipoPrimitivo.I64
                        else:
                            alert = "Error en rango, no se puede iterar al reves"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                            print(alert)

                    else:
                        alert = "Error este tipo de dato no se puede iterar"
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)
                else:
                    alert = "Error en declaracion de rango"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)
            else:
                #! for para arreglos
                if type1 in [tipoPrimitivo.ARREGLO, tipoPrimitivo.VECTOR]:
                    arreglo = data1.valor
                    tipin = arreglo[0].tipo
                else:
                    alert = "Error la expresion no es de tipo VECTOR"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)
                    # ! aqui va error
            if tipin is not None:
                entorno_for = Entorno(entorno, True, entorno.flag_return, True)
                Tabla_Simbolos.append(entorno_for)
                variable = Variable(tipin, self.id, arreglo[0].valor, self.fila, True)
                entorno_for.nueva_variable(variable)
                for i in range(len(arreglo)):
                    var_index = entorno_for.buscar_variable(self.id)
                    var_index.valor = arreglo[i].valor
                    entorno_for.editar_variable(self.id, var_index)

                    # ! se iteran instrucciones

                    for instruc in self.instrucciones:

                        res = instruc.ejecutar(entorno_for)

                        if res:
                            if isinstance(res, Return) and entorno_for.flag_return:
                                return res
                            elif isinstance(res, Continue) and entorno_for.flag_continue:
                                break
                            elif isinstance(res, Break) and entorno_for.flag_break:
                                return None
                            elif isinstance(res, Return) and not entorno_for.flag_return:
                                alert = "Error el RETURN solo puede estar dentro de funciones"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)

                        else:
                            pass

            else:
                alert = "Error no se puede iterar este tipo de VECTOR"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)
        else:
            alert = "Error el vector no ha sido declarado"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
