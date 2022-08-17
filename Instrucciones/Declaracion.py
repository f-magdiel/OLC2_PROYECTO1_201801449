from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Variable import Variable
from Entorno.Entorno import Entorno


class DeclaracionVariable(Instruccion):

    def __init__(self, fila, tipo, nombre, expresion, mutable):
        super().__init__(fila)
        self.fila = fila
        self.mutable = mutable
        self.tipo = tipo
        self.nombre = nombre
        self.expresion = expresion

    def ejecutar(self, entorno: Entorno):

        if (self.tipo and self.nombre and self.expresion):
            var = entorno.buscar_variable_entorno(self.nombre)
            if not (var):
                expre = self.expresion.ejecutar(entorno)
                if (expre):
                    if not (isinstance(expre.valor, list)):

                        if (expre.tipo == self.tipo and self.tipo != tipoPrimitivo.STRING):  # Si es el mismo tipo
                            variable = Variable(self.tipo, self.nombre, expre.valor, self.fila, self.mutable)
                            entorno.nueva_variable(variable)

                        # elif (self.tipo == tipoPrimitivo.STR and expre.tipo == tipoPrimitivo.STRING):
                        #     variable = Variable(self.tipo, self.nombre, expre.valor, self.fila, self.mutable)
                        #     entorno.nueva_variable(variable)

                        elif (self.tipo == tipoPrimitivo.NULO):

                            if expre.tipo == tipoPrimitivo.TOS or expre.tipo == tipoPrimitivo.TOW:
                                variable = Variable(tipoPrimitivo.STRING, self.nombre, expre.valor, self.fila, self.mutable)
                                entorno.nueva_variable(variable)
                            else:
                                variable = Variable(expre.tipo, self.nombre, expre.valor, self.fila, self.mutable)
                                entorno.nueva_variable(variable)

                        elif((expre.tipo == tipoPrimitivo.TOS or expre.tipo == tipoPrimitivo.TOW) and self.tipo == tipoPrimitivo.STRING):
                            variable = Variable(expre.tipo, self.nombre, expre.valor, self.fila, self.mutable)
                            entorno.nueva_variable(variable)
                        else:
                            print("El tipo {} y la expresion {} no coinciden")

                    else:
                        msg_error = 'La variable no puede almacenar un arreglo'
                        print(msg_error)
            else:
                msg_error = "Ya existe una variable con el nombre '{}' en la tabla de simbolos.".format(self.nombre)
                print(msg_error)
