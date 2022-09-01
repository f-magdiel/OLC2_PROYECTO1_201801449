from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Enumeradas.Primitivo import tipoPrimitivo


class CreacionVector(Instruccion):
    def __init__(self, fila, expresion=None):
        super().__init__(fila)
        self.expresion = expresion


    def ejecutar(self, entorno: Entorno):

        if self.expresion is None:
            return Primitiva(self.fila, tipoPrimitivo.VECTOR, [])
        else:
            data = self.expresion.ejecutar(entorno)
            #print("data",data.valor)
            if data:
                tipo = data.tipo
                if tipo == tipoPrimitivo.I64:
                    valor = data.valor
                    if valor > 0:
                        return Primitiva(self.fila, tipoPrimitivo.VECTOR, [], data.valor)
                    else:
                        pass
                else:
                    pass
            else:
                pass
