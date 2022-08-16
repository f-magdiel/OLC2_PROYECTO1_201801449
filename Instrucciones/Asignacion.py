from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Enumeradas.Primitivo import tipoPrimitivo


class AsignacionVariable(Instruccion):
    def __init__(self, fila, nombre, expresion):
        super().__init__(fila)
        self.nombre = nombre
        self.expresion = expresion

    def ejecutar(self, entorno: Entorno):
        if (self.nombre and self.expresion):
            variable = entorno.buscar_variable(self.nombre)
            if (variable):
                expre = self.expresion.ejecutar(entorno)
                if (expre):
                    if not (isinstance(expre.valor, list)):
                        if (expre.tipo == variable.tipo and expre.tipo != tipoPrimitivo.STRING):  # Si es el mismo tipo
                            nueva_variable = Variable(variable.tipo, variable.nombre, self.expresion, self.fila, variable.mutable)
                            entorno.editar_variable(variable.nombre, nueva_variable)


                        elif ((expre.tipo == tipoPrimitivo.TOS or expre.tipo == tipoPrimitivo.TOW) and variable.tipo == tipoPrimitivo.STRING):# si es tipo string o str
                            nueva_variable = Variable(variable.tipo, variable.nombre, self.expresion, self.fila, variable.mutable)
                            entorno.editar_variable(variable.nombre, nueva_variable)


                        elif(variable.tipo == tipoPrimitivo.STR and expre.tipo == tipoPrimitivo.STRING):
                            nueva_variable = Variable(variable.tipo, variable.nombre, self.expresion, self.fila, variable.mutable)
                            entorno.editar_variable(variable.nombre, nueva_variable)


                        else:
                            print("El tipo {} y la expresion {} no coinciden")
