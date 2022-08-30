from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Enumeradas.Primitivo import tipoPrimitivo

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
            if count_sep == len(self.expresiones):  # ? validar que tenga los mismos {} y parametros
                for i in self.expresiones:
                    val = i.ejecutar(entorno)
                    if val.tipo == tipoPrimitivo.ARREGLO:
                        arr = []
                        self.transformar(val.valor, arr)
                        cadena = cadena.replace("{}", str(arr), 1)

                    else:
                        cadena = cadena.replace("{}", str(val.valor), 1)

                print(cadena)

        elif self.expresion:
            expre = self.expresion.ejecutar(entorno)
            if expre and expre.tipo == tipoPrimitivo.STR:
                print(expre.valor)
            else:
                print("Debe llevar un formato")
                # TODO

    def transformar(self, valor, arreglo):  # Convierte un arreglo de primitivas en un arreglo con valores normales
        if isinstance(valor, list):
            for elemento in valor:
                if isinstance(elemento.valor, list):
                    arreglo_hijo = []
                    self.transformar(elemento.valor, arreglo_hijo)
                    arreglo.append(arreglo_hijo)
                else:
                    arreglo.append(elemento.valor)
