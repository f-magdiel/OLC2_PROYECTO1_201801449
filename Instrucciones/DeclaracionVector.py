from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Variable import Variable

class DeclaracionVector(Instruccion):
    def __init__(self, fila, id, expresion, tipo, mutable):
        super().__init__(fila)
        self.id = id
        self.expresion = expresion
        self.tipo = tipo
        self.mutable = mutable

    def ejecutar(self, entorno: Entorno):
        data = self.expresion.ejecutar(entorno)

        if data:
            if data.tipo == tipoPrimitivo.VECTOR:
                # ! recorrer arreglo
                iguales = True
                # for i in range(len(data.valor)):
                #     if data.tipo != self.tipo:
                #         iguales = False
                #         break

                #validar
                if iguales:
                    variable = Variable(tipoPrimitivo.VECTOR, self.id, data.valor, self.fila, self.mutable)
                    entorno.nueva_variable(variable)
                else:
                    pass
            else:
                pass
        else:
            pass
