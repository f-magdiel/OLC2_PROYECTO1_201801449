from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.OperadorAritmetica import OPERADOR_ARITMETICO
from Enumeradas.Primitivo import tipoPrimitivo
from Expresiones.Primitiva import Primitiva
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class Aritmetica(Instruccion):
    def __init__(self, fila, exp1, operador, exp2, tipoOP):
        super().__init__(fila)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.tipoOP = tipoOP

    def ejecutar(self, entorno: Entorno):
        if self.exp1 and self.exp2 and self.operador:  # ! Que no venga vacío
            expresion1 = self.exp1.ejecutar(entorno)
            expresion2 = self.exp2.ejecutar(entorno)

            if expresion1 and expresion2:
                if not (isinstance(expresion1.valor, list) or isinstance(expresion2.valor, list)):
                    # ! Operacion SUMA
                    if self.operador == OPERADOR_ARITMETICO.MAS:
                        if expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:  # ! suma de float
                            resultado = round(float(expresion1.valor) + float(expresion2.valor), 2)
                            return Primitiva(self.fila, tipoPrimitivo.F64, resultado)

                        elif expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64:  # ! Suma de enteros
                            resultado = int(expresion1.valor) + int(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.I64, resultado)

                        elif (expresion1.tipo == tipoPrimitivo.TOS or expresion1.tipo == tipoPrimitivo.TOW) and expresion2.tipo == tipoPrimitivo.STR:  # ! para concatenar string
                            resultado = str(expresion1.valor) + str(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.TOS, resultado)

                        else:
                            alert = "Error al operar operaciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                    # ! Operacion Resta
                    elif self.operador == OPERADOR_ARITMETICO.MENOS:

                        if expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:  # ! resta de float
                            resultado = round(float(expresion1.valor) - float(expresion2.valor), 2)
                            return Primitiva(self.fila, tipoPrimitivo.F64, resultado)

                        elif expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64:  # ! resta para entero
                            resultado = int(expresion1.valor) - int(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.I64, resultado)

                        else:
                            alert = "Error al operar operaciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                    # ! Operacion Multiplicacion
                    elif self.operador == OPERADOR_ARITMETICO.POR:
                        if expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:  # ! multiplicacion de float
                            resultado = round(float(expresion1.valor) * float(expresion2.valor), 2)
                            return Primitiva(self.fila, tipoPrimitivo.F64, resultado)

                        elif expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64:  # ! multiplicacion de entero
                            resultado = int(expresion1.valor) * int(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.I64, resultado)

                        else:
                            alert = "Error al operar operaciones "
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    # ! Operacion division
                    elif self.operador == OPERADOR_ARITMETICO.DIVIDIDO:
                        if expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:  # ! division de float
                            if expresion2.valor != 0:
                                resultado = round(float(expresion1.valor) / float(expresion2.valor), 2)
                                return Primitiva(self.fila, tipoPrimitivo.F64, resultado)
                            else:
                                alert = "Error no se puede dividir entre 0"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)
                        elif expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64:  # ! division de entero
                            if expresion2.valor!=0:
                                resultado = round(int(expresion1.valor) / int(expresion2.valor), 2)
                                return Primitiva(self.fila, tipoPrimitivo.I64, resultado)
                            else:
                                alert = "Error no se puede dividir entre 0"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                print(alert)
                        else:
                            alert = "Error al operar operaciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                    # !Operacion modulo
                    elif self.operador == OPERADOR_ARITMETICO.MODULO:
                        if expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:  # ! modulo de float
                            resultado = round(float(expresion1.valor) % float(expresion2.valor), 2)
                            return Primitiva(self.fila, tipoPrimitivo.F64, resultado)

                        elif expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64:  # ! modulo de entero
                            resultado = int(expresion1.valor) % int(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.I64, resultado)

                        else:
                            alert = "Error al operar operaciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                    #!Operacion de potencia para float
                    elif self.operador == OPERADOR_ARITMETICO.POTENCIAF and self.tipoOP is not None:
                        if self.tipoOP == tipoPrimitivo.F64 and expresion1.tipo == tipoPrimitivo.F64 and expresion2.tipo == tipoPrimitivo.F64:  # ! Potencia de float
                            resultado = round(float(expresion1.valor) ** float(expresion2.valor), 2)
                            return Primitiva(self.fila, tipoPrimitivo.F64, resultado)
                        else:
                            alert = "Error al operar operaciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    #!Operacion de potencia para int
                    elif self.operador == OPERADOR_ARITMETICO.POTENCIA and self.tipoOP is not None:
                        if self.tipoOP == tipoPrimitivo.I64 and expresion1.tipo == tipoPrimitivo.I64 and expresion2.tipo == tipoPrimitivo.I64:  # !Potencia de entero
                            resultado = int(expresion1.valor) ** int(expresion2.valor)
                            return Primitiva(self.fila, tipoPrimitivo.I64, resultado)
                        else:
                            alert = "Error al operar operaciones"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                else:
                    alert = "Error tipo incompatible para realizar operaciones"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error el tipo de expresiones es incompatible"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
