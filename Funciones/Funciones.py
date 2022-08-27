from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Abstracta.Instruccion import Instruccion
from Entorno.Funcion import Funcion as ObjetoFuncion
from Entorno.Entorno import Entorno



class Parametros():
    def __init__(self, tipo, nombre):  # * Aquí debe ir arreglos
        self.tipo = tipo
        self.nombre = nombre


class Funciones(Instruccion):
    def __init__(self, fila, tipo, nombre, parametros, instrucciones):
        super().__init__(fila)
        self.tipo = tipo
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones


    def ejecutar(self, entorno: Entorno):
        if self.tipo and self.nombre and self.instrucciones:
            f = entorno.buscar_funcion_entorno(self.nombre)

            # si recibe true-false
            if not (f):
                parametros_correctos = True

                for parametro in self.parametros:
                    nombre = parametro.nombre
                    contador = 0
                    for p in self.parametros:  # valido que no venga 2 veces el parametro osea(x,x)
                        if (p.nombre == nombre):
                            contador += 1
                    if (contador > 1):
                        parametros_correctos = False  # aqui truena

                if (parametros_correctos):  # este es para menor a 1 parametro
                    instrucciones_correctas = True
                    hubo_return = False
                    # for instruccion in self.instrucciones:
                    # if (instruccion):
                    # aqui validaremos que si retorno o no algun dato o solo se ejecuta.

                    funcion = ObjetoFuncion(self.fila, self.tipo, self.nombre, self.parametros, self.instrucciones, )  # aqui creo el objeto funcion
                    entorno.nueva_funcion(funcion)  # aqui guardo la funcion
                    #print("Se crea funciones")
