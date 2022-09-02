from Abstracta.Instruccion import Instruccion
from Entorno.Variable import Variable
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Enumeradas.NativeVectores import NATIVE_VECTORES
from Enumeradas.Primitivo import tipoPrimitivo


class NativasVectores(Instruccion):
    def __init__(self, fila, id, funcion, expresion1=None, expresion2=None):
        super().__init__(fila)
        self.id = id
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.funcion = funcion

    def ejecutar(self, entorno: Entorno):

        if NATIVE_VECTORES.LEN == self.funcion:
            # ! Busco el nombre = id
            var = self.id.ejecutar(entorno)
            tam = len(var.valor)
            return Primitiva(self.fila, tipoPrimitivo.I64, tam)
        elif NATIVE_VECTORES.CAPACITY == self.funcion:
            var = entorno.buscar_variable(self.expresion1.nombre)

        elif NATIVE_VECTORES.PUSH == self.funcion:
            var = entorno.buscar_variable(self.id.nombre)
            var.valor.append(self.expresion1)
            entorno.editar_variable(self.id.nombre, var)

        elif NATIVE_VECTORES.CONTAINS == self.funcion:
            pass
        elif NATIVE_VECTORES.REMOVE == self.funcion:
            var = entorno.buscar_variable(self.id.nombre)
            pos = self.expresion1.ejecutar(entorno)
            var.valor.pop(pos.valor)
            entorno.editar_variable(self.id.nombre, var)

        elif NATIVE_VECTORES.REMOVE_EXPRE == self.funcion:
            var = entorno.buscar_variable(self.id.nombre)
            pos = self.expresion1.ejecutar(entorno)
            newvariable = var.valor.pop(pos.valor)
            entorno.editar_variable(self.id.nombre, var)
            return Primitiva(self.fila, pos.tipo, newvariable.valor)

        elif NATIVE_VECTORES.INSERT == self.funcion:
            var = entorno.buscar_variable(self.id.nombre)
            pos = self.expresion1.ejecutar(entorno)
            var.valor.insert(pos.valor, self.expresion2)
            entorno.editar_variable(self.id.nombre, var)
        else:
            pass
            # ! Errores
