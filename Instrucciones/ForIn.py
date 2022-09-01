import Expresiones
from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Entorno.Variable import Variable
from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue


class ForIn(Instruccion):
    def __init__(self, fila, id, exp1, instrucciones, exp2=None):
        super().__init__(fila)
        self.id = id
        self.exp1 = exp1
        self.exp2 = exp2
        self.instrucciones = instrucciones

    def ejecutar(self, entorno: Entorno):
        data1 = self.exp1.ejecutar(entorno)
        if data1:
            # ! obtener de una el tipo
            type1 = data1.tipo
            arreglo = []
            tipin = None
            # ! validar si viene expre2
            if self.exp2:
                print(self.exp2)
                data2 = self.exp2.ejecutar(entorno)
                if data2:
                    type2 = data2.tipo
                    # ! ambos tienen que ser de tipo i64
                    if type1 == tipoPrimitivo.I64 and type2 == tipoPrimitivo.I64:
                        # ! proceso del ciclo for
                        if data2.valor > data1.valor:  # ! validar que expre2 sea mayor que expre1
                            for val in range(data1.valor, data2.valor):
                                arreglo.append(Primitiva(self.fila, tipoPrimitivo.I64, val))

                            tipin = tipoPrimitivo.I64
                        else:
                            pass

                    else:
                        pass
                else:
                    pass
            else:

                if type1 in [tipoPrimitivo.ARREGLO, tipoPrimitivo.VECTOR]:
                    arreglo = data1.valor

                    tipin = type1
                else:
                    pass
                    # ! aqui va error
            if tipin is not None:
                entorno_for = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
                variable = Variable(arreglo[0].valor, self.id, tipin, self.fila, True)
                entorno_for.nueva_variable(variable)
                for i in range(len(arreglo)):
                    var_index = entorno_for.buscar_variable(self.id)
                    var_index.valor = arreglo[i].valor
                    entorno_for.editar_variable(self.id, variable)

                    # ! se iteran instrucciones

                    for instruc in self.instrucciones:
                        if instruc:
                            res = instruc.ejecutar(entorno_for)
                            if res:
                                if isinstance(res, Return):
                                    pass
                                elif isinstance(res, Continue):
                                    pass
                                elif isinstance(res, Break):
                                    pass

                            else:
                                pass
                        else:
                            pass
            else:
                pass
        else:
            pass
