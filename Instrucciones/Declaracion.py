from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Variable, Entorno


class DeclaracionVariable(Instruccion):

    def __init__(self, fila, tipo, nombre, expresion, mutable):
        super().__init__(fila)
        self.fila = fila
        self.mutable = mutable
        self.tipo = tipo
        self.nombre = nombre
        self.expresion = expresion

    def ejecutar(self, entorno: Entorno):
        print("Fila {}".format(self.fila))
        print("Mut {}".format(self.mutable))
        print("Se declara {}".format(self.tipo))
        print("Se declara {}".format(self.nombre))
        print("Se declara {}".format(self.expresion))
