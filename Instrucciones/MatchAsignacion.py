from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Enumeradas.TipoMatch import TIPO_MATCH
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR

class MatchAsignacion(Instruccion):
    def __init__(self, fila, expresion, listaexpresion: list):
        super().__init__(fila)
        self.expresion = expresion
        self.listaexpresion = listaexpresion
        self.TipoGlobal = tipoPrimitivo.NULO

    def ejecutar(self, entorno: Entorno):
        contador_e = 0
        contador_t = 0

        if self.expresion and self.expresion:
            valorexpre = self.expresion.ejecutar(entorno)  # ! Se ejecuta la condicion
            if valorexpre:
                self.TipoGlobal = valorexpre.tipo  # ! se define el tipo de la condicion
            else:
                alert = "Error expresion no definido"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

            for elem in self.listaexpresion:
                for i in range(len(elem)):
                    if i == 0 and elem[i]:  # ! este if es para recorrer expresiones
                        for j in elem[0]:
                            if j != '_':
                                expre = j.ejecutar(entorno)
                                contador_t += 1
                                if expre:
                                    if expre.tipo == self.TipoGlobal:
                                        contador_e += 1
                                else:
                                    alert = "Error expresion no definido"
                                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                                    print(alert)

            if contador_e == contador_t:
                for i in range(len(self.listaexpresion)):
                    for j in range(len(self.listaexpresion[i])):

                        if self.listaexpresion[i][j] == TIPO_MATCH.MATCHBARRAS:
                            # print(self.listaglobal[i][0])
                            for k in range(len(self.listaexpresion[i][0])):
                                val = self.listaexpresion[i][0][k].ejecutar(entorno)
                                if val.valor == valorexpre.valor:
                                    nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                    Tabla_Simbolos.append(nuevo_entorno)
                                    for l in range(len(self.listaexpresion[i][1])):
                                        var = self.listaexpresion[i][1][l].ejecutar(nuevo_entorno)

                                        return Primitiva(self.fila, var.tipo, var.valor)

                        elif self.listaexpresion[i][j] == TIPO_MATCH.MATCHDEFAULT:
                            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                            Tabla_Simbolos.append(nuevo_entorno)
                            for l in range(len(self.listaexpresion[i][1])):
                                var = self.listaexpresion[i][1][l].ejecutar(nuevo_entorno)
                                return Primitiva(self.fila, var.tipo, var.valor)
            else:
                alert = "Error los tipos de los brazos son incompatibles"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)
        else:
            alert = "Error expresion no definido"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))