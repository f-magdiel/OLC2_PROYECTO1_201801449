from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Enumeradas.TipoMatch import TIPO_MATCH

class Match(Instruccion):
    def __init__(self, fila, expresion, listaglobal: list):
        super().__init__(fila)
        self.expresion = expresion
        self.listaglobal = listaglobal
        self.tipoGlobalMatch = tipoPrimitivo.NULO

    def ejecutar(self, entorno: Entorno):
        contador_e = 0
        contador_t = 0

        if self.expresion and self.listaglobal:  # ! Mas de algo tiene que venir
            valorexpre = self.expresion.ejecutar(entorno)
            self.tipoGlobalMatch = valorexpre.tipo

            for elem in self.listaglobal:
                for i in range(len(elem)):
                    if i == 0 and elem[i]:  # ! este if es para recorrer expresiones
                        for j in elem[0]:
                            if j != '_':
                                expre = j.ejecutar(entorno)
                                contador_t += 1
                                if expre.tipo == self.tipoGlobalMatch:
                                    contador_e += 1


            if contador_e == contador_t:  # ! Cumple con todas las estructuras match brazos, rango, barra y 1 default
                for i in range(len(self.listaglobal)):
                    for j in range(len(self.listaglobal[i])):
                        #! Se busca el tipo primero
                        if self.listaglobal[i][j] == TIPO_MATCH.MATCHRANGO:
                            #! se valuan las expresiones
                            val1 = self.listaglobal[i][0][0].ejecutar(entorno)
                            val2 = self.listaglobal[i][0][1].ejecutar(entorno)
                            #     2        >=      1                    2          <=        3
                            if valorexpre.valor >= val1.valor  and valorexpre.valor  <= val2.valor:
                                nuevo_entorno = Entorno(entorno,entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                for k in range(len(self.listaglobal[i][1])):
                                    self.listaglobal[i][1][k].ejecutar(nuevo_entorno)

                                return #! Se usa retun para multiples bucles

                        elif self.listaglobal[i][j] == TIPO_MATCH.MATCHBARRAS:
                            #print(self.listaglobal[i][0])
                            for k in range(len(self.listaglobal[i][0])):
                                val = self.listaglobal[i][0][k].ejecutar(entorno)
                                if val.valor == valorexpre.valor:
                                    nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                                    for l in range(len(self.listaglobal[i][1])):
                                        self.listaglobal[i][1][l].ejecutar(nuevo_entorno)

                                    return

                        elif self.listaglobal[i][j] == TIPO_MATCH.MATCHDEFAULT:
                            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                            for l in range(len(self.listaglobal[i][1])):
                                self.listaglobal[i][1][l].ejecutar(nuevo_entorno)

