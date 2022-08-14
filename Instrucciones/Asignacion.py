from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Enumeradas.Primitivo import tipoPrimitivo

class Asignacion(Instruccion):
    def __init__(self, fila, nombre, expresion):
        super().__init__(fila)
        self.nombre = nombre
        self.expresion = expresion

    def ejecutar(self, entorno: Entorno):
        if(self.nombre and self.expresion):
            variable =entorno.buscar_variable(self.nombre)
            if(variable):
                expre =self.expresion.ejecutar(entorno)
                if (expre):
                    if not(isinstance(expre.valor, list)):
                        if (expre.tipo == self.tipo):  # Si es el mismo tipo
                            variable = Variable(self.tipo, self.nombre, self.expresion, self.fila, self.mutable)
                            entorno.nueva_variable(variable)

                        elif (self.tipo == tipoPrimitivo.STR and expre.tipo == tipoPrimitivo.STRING):
                            variable = Variable(self.tipo, self.nombre, self.expresion, self.fila, self.mutable)
                            entorno.nueva_variable(variable)

                        elif (self.tipo == tipoPrimitivo.NULO):

                            variable = Variable(expre.tipo, self.nombre, self.expresion, self.fila, self.mutable)
                            entorno.nueva_variable(variable)

                        elif(expre.tipo == tipoPrimitivo.TOS or expre.tipo == tipoPrimitivo.TOW):
                            print("Expre tostring {}", expre.tipo)
                            variable = Variable(expre.tipo, self.nombre, self.expresion, self.fila, self.mutable)

                        else:
                            print("El tipo {} y la expresion {} no coinciden")

