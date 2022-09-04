from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Abstracta.Instruccion import Instruccion
from Entorno.Funcion import Funcion as ObjetoFuncion
from Entorno.Entorno import Entorno
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


class Parametros():
    def __init__(self, tipo, nombre, si_arreglo, dimensiones,si_vector=False):  # * Aquí debe ir arreglos
        self.tipo = tipo
        self.nombre = nombre
        self.si_arreglo = si_arreglo
        self.dimensiones = dimensiones
        self.si_vector = si_vector


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
                    funcion = ObjetoFuncion(self.fila, self.tipo, self.nombre, self.parametros, self.instrucciones, )  # aqui creo el objeto funcion
                    entorno.nueva_funcion(funcion)
                else:
                    alert = "Error se repite parametros de funciones"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)

            else:
                alert = "Error no se encuentra la funcion "
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

        else:
            alert = "Error funciones viene vacio"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)