from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class IfAsignacion(Instruccion):
    def __init__(self, fila, expresion, bloque_expresiones: list, expresion_else: list):
        super().__init__(fila)
        self.expresion = expresion
        self.bloque_expresiones = bloque_expresiones
        self.expresion_else = expresion_else
        self.tipoGlobal = tipoPrimitivo.NULO

    def ejecutar(self, entorno: Entorno):
        if self.expresion and self.bloque_expresiones:  # ! Que no vengan vacios
            expre = self.expresion.ejecutar(entorno)
            if expre:
                if expre.tipo == tipoPrimitivo.BOOL:
                    nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                    Tabla_Simbolos.append(nuevo_entorno)
                    self.obtenerTipoGlobal(nuevo_entorno)
                    if expre.valor:

                        contador_expres = 0
                        for expres in self.bloque_expresiones:
                            if expres:
                                exp = expres.ejecutar(nuevo_entorno)
                                if exp:
                                    if exp.tipo == self.tipoGlobal:
                                        contador_expres += 1
                                    else:
                                        alert = "Error el tipo de elemento es incompatible"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                else:
                                    alert = "Error al ejecutar expresion"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                            else:
                                alert = "Error al ejecutar expresion array"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                        if contador_expres == len(self.bloque_expresiones):
                            res = self.bloque_expresiones[contador_expres - 1].ejecutar(nuevo_entorno)
                            return Primitiva(self.fila, self.tipoGlobal, res.valor)
                        else:
                            alert = "Error las expresiones no son compatibles"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    else:
                        if self.expresion_else:
                            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                            Tabla_Simbolos.append(nuevo_entorno)
                            # ! Se ejecutan las expresiones y validar que se uno o mas
                            # Segundo for
                            contador_expres = 0
                            for expres in self.expresion_else:
                                if expres:
                                    exp = expres.ejecutar(nuevo_entorno)
                                    if exp:
                                        if exp.tipo == self.tipoGlobal:
                                            contador_expres += 1
                                        else:
                                            alert = "Error el tipo de elemento es incompatible"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                    else:
                                        alert = "Error al ejecutar expresion"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                else:
                                    alert = "Error error al ejecutar expresion array"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                            if contador_expres == len(self.expresion_else):
                                res = self.expresion_else[contador_expres - 1].ejecutar(nuevo_entorno)
                                return Primitiva(self.fila, self.tipoGlobal, res.valor)
                            else:
                                alert = "Error las expresiones no son compatibles"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                else:

                    alert = "Error If asignacion no es de tipo BOOL"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error al ejecutar expresion"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

        else:
            alert = "Error las expresiones vienen vacías"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))



    def obtenerTipoGlobal(self, nuevo_entorno):
        for ite in self.bloque_expresiones:
            if ite:
                exp = ite.ejecutar(nuevo_entorno)
                self.tipoGlobal = exp.tipo
                break


class ElseIfAsignacion(Instruccion):
    def __init__(self, fila, expresion, bloque_expresiones: list, expresion_elseif: list, expresion_else: list):
        super().__init__(fila)
        self.expresion = expresion
        self.bloque_expresiones = bloque_expresiones
        self.expresion_elseif = expresion_elseif
        self.expresion_else = expresion_else
        self.tipoGlobal = tipoPrimitivo.NULO

    def ejecutar(self, entorno):
        if self.expresion:
            expre = self.expresion.ejecutar(entorno)
            if expre:
                if expre.tipo == tipoPrimitivo.BOOL:
                    nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return,entorno.flag_continue)
                    Tabla_Simbolos.append(nuevo_entorno)
                    self.obtenerTipoGlobal(nuevo_entorno)
                    if expre.valor:
                        contador_expres = 0
                        for expres in self.bloque_expresiones:
                            if expres:
                                exp = expres.ejecutar(nuevo_entorno)
                                if exp:
                                    if exp.tipo == self.tipoGlobal:
                                        contador_expres += 1
                                    else:
                                        alert = "Error el tipo no es compatible"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                else:
                                    alert = "Error el tipo no es compatible"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                            else:
                                alert = "Error el ejecutar elemento array"
                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                        if contador_expres == len(self.bloque_expresiones):
                            res = self.bloque_expresiones[contador_expres - 1].ejecutar(nuevo_entorno)
                            return Primitiva(self.fila, self.tipoGlobal, res.valor)
                        else:
                            alert = "Error las expresiones no son compatibles"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    else:
                        cumple = False
                        for else_if in self.expresion_elseif:  # aqui me meto a la lista completa  ---> [[cada elseif],[],[]]
                            condicion_else_if = else_if[0].ejecutar(entorno)  # [condicionales,[listaExpre]], ose que vy a ejecitar la condicionales
                            if (condicion_else_if):  # si no sigue dando la vuelta
                                if (condicion_else_if.tipo == tipoPrimitivo.BOOL):

                                    if (condicion_else_if.valor):  # aqui solo valido que si es false o true si es false no hace nada y sigue con la vuelta
                                        cumple = True  # aqui le digo que mas de algun condcion cumplio
                                        nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                        Tabla_Simbolos.append(nuevo_entorno)
                                        contador_expre = 0
                                        for instruccion_else_if in else_if[1]:
                                            if (instruccion_else_if):
                                                instr = instruccion_else_if.ejecutar(nuevo_entorno)
                                                if instr.tipo == self.tipoGlobal:
                                                    contador_expre += 1
                                                else:
                                                    alert = "Error el tipo no es compatible"
                                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                        if contador_expre == len(else_if[1]):
                                            resF = else_if[1][contador_expre - 1].ejecutar(nuevo_entorno)
                                            return Primitiva(self.fila, self.tipoGlobal, resF.valor)
                                        else:
                                            alert = "Error las expresiones no son compatibles"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                        break  # se sale del for completamente
                                else:
                                    alert = "Error el tipo no es compatible"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                        if not cumple:

                            if self.expresion_else:
                                nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                Tabla_Simbolos.append(nuevo_entorno)
                                contador_expres = 0
                                for expres in self.expresion_else:
                                    if expres:
                                        exp = expres.ejecutar(nuevo_entorno)
                                        if exp:
                                            if exp.tipo == self.tipoGlobal:
                                                contador_expres += 1
                                            else:
                                                alert = "Error el tipo no es compatible"
                                                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                        else:
                                            alert = "Error la expresion está vacía"
                                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                                    else:
                                        alert = "Error la expresion está vacía"
                                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                                if contador_expres == len(self.expresion_else):
                                    res = self.expresion_else[contador_expres - 1].ejecutar(nuevo_entorno)
                                    return Primitiva(self.fila, self.tipoGlobal, res.valor)
                                else:
                                    alert = "Error las expresiones no son compatibles"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                else:
                    alert = "Error no es de tipo BOOL"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error al ejecutar expresion"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

        else:
            alert = "Error la expresion viene vacía"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


    def obtenerTipoGlobal(self, nuevo_entorno):
        for ite in self.bloque_expresiones:
            if ite:
                exp = ite.ejecutar(nuevo_entorno)
                if exp:
                    self.tipoGlobal = exp.tipo
                else:
                    alert = "Error el tipo no es compatible"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                break
