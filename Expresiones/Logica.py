from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Enumeradas.OperadorLogico import OPERADOR_LOGICO
from Expresiones.Primitiva import Primitiva
from Entorno.Entorno import Entorno
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class Logica(Instruccion):
    def __init__(self, fila, expresion1, operador, expresion2):
        super().__init__(fila)
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.operador = operador

    def ejecutar(self, entorno: Entorno):
        if self.expresion1 and self.expresion2 and self.operador:
            expre1 = self.expresion1.ejecutar(entorno)
            expre2 = self.expresion2.ejecutar(entorno)
            if expre1 and expre2:
                if expre1.tipo == tipoPrimitivo.BOOL and expre2.tipo == tipoPrimitivo.BOOL:
                    # ! para or
                    if self.operador == OPERADOR_LOGICO.OR:
                        resultado = expre1.valor or expre2.valor
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    # ! para and
                    elif self.operador == OPERADOR_LOGICO.AND:
                        resultado = expre1.valor and expre2.valor
                        return Primitiva(self.fila, tipoPrimitivo.BOOL, resultado)
                    else:
                        alert = "Error al realizar operaciones logicas"
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                else:
                    alert = "Error al realizar operaciones logicas, expresiones incompatibles"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

            else:
                alert = "Error al realizar operaciones logicas"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

        else:
            alert = "Error al realizar operaciones logicas"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
