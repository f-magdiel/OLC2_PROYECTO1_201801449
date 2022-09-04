from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR
listimpresion = []


class Imprimir(Instruccion):
    def __init__(self, fila, expresion, expresiones: list):
        super().__init__(fila)
        self.expresion = expresion
        self.expresiones = expresiones

    def ejecutar(self, entorno: Entorno):

        if self.expresion is not None and self.expresiones is not None:
            expre = self.expresion.ejecutar(entorno)  # ? Primero ejecuta solo la expresion
            cadena = str(expre.valor)
            count_sep = str(expre.valor).count("{}")

            if expre:
                if count_sep == len(self.expresiones):  # ? validar que tenga los mismos {} y parametros
                    for i in self.expresiones:
                        val = i.ejecutar(entorno)

                        if val:
                            if val.tipo == tipoPrimitivo.ARREGLO or val.tipo == tipoPrimitivo.VECTOR:
                                arr = []

                                self.transformar(val.valor, arr)
                                cadena = cadena.replace("{}", str(arr), 1)

                            else:
                                cadena = cadena.replace("{}", str(val.valor), 1)
                        else:
                            alert = "Error al imprimir expresion no compatible"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


                    print(cadena)
                else:
                    alert = "Error la impresion debe de tener el mismo {} que los argumentos"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            else:
                alert = "Error al imprimir expresion"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

        elif self.expresion:
            expre = self.expresion.ejecutar(entorno)

            if expre:
                if expre.tipo == tipoPrimitivo.STR:
                    print(expre.valor)
                else:
                    alert = "Error la imprimir debe de llevar un formato"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            else:
                alert = "Error al imprimir expresion porque viene vacía"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

        else:
            alert = "Error no puede venir vacio el println"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))


    def transformar(self, valor, arreglo):  # Convierte un arreglo de primitivas en un arreglo con valores normales
        if isinstance(valor, list):
            for elemento in valor:

                if isinstance(elemento.valor, list):
                    arreglo_hijo = []
                    self.transformar(elemento.valor, arreglo_hijo)
                    arreglo.append(arreglo_hijo)
                else:

                    arreglo.append(elemento.valor)
