from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Entorno.Variable import Variable
from Enumeradas.Primitivo import tipoPrimitivo


class DeclaracionArreglos(Instruccion):
    def __init__(self, fila, nombre, tipo_arreglo: list, expresion, mutable):
        super().__init__(fila)
        self.nombre = nombre
        self.tipo_arreglo = tipo_arreglo
        self.expresion = expresion
        self.mutable = mutable

    def ejecutar(self, entorno: Entorno):
        # Interpretar la expresión y obtener el dato resultante
        dato = self.expresion.ejecutar(entorno)
        # Validar que no haya ocurrido un error en la expresión al calcular el dato (None)
        if dato:
            # Obtener el tipo del dato
            tipo_dato = dato.tipo
            # Validar que el tipo de dato sea un arreglo
            if tipo_dato == tipoPrimitivo.ARREGLO:
                # Transformar a un arreglo de valores primitivos las dimensiones del arreglo
                dim_arr = []
                self.transformar(self.tipo_arreglo[1:], dim_arr)
                # Recorrer el arreglo de dimensiones y verificar que sean solo enteros >= 0
                correctas = True
                for dimension in dim_arr:
                    if not isinstance(dimension, int):
                        correctas = False
                        break
                    elif dimension < 0:
                        correctas = False
                        break
                # Validar que el arreglo de dimensiones sea solo de enteros >= 0
                if correctas:
                    # Obtener un listado de las dimensiones del dato
                    dim_dato = []
                    self.obtener_dimensiones(dato.valor, dim_dato)
                    # dim_dato.reverse()
                    # Validar que ambos arreglos tengan el mismo tamaño
                    if len(dim_arr) == len(dim_dato):
                        # Recorrer ambos arreglos dimensionales para verificar que sean iguales
                        iguales = True
                        for i in range(len(dim_arr)):
                            if dim_arr[i] != dim_dato[i]:
                                iguales = False
                                break
                        # Validar si son las mismas dimensiones
                        if iguales:
                            # Obtener el tipo primitivo de la variable
                            tipo_prim_var = self.tipo_arreglo[0]
                            # Obtener el tipo primitivo del dato
                            tipo_prim_dato = self.obtener_tipo(dato)
                            # Validar que el tipo de la variable sea compatible con el tipo del dato
                            if tipo_prim_dato in [tipo_prim_var, tipoPrimitivo.ARREGLO]:
                                variable = Variable(tipoPrimitivo.ARREGLO, self.nombre, dato.valor, self.fila, self.mutable)
                                #print(variable.valor[0].valor[0].valor)
                                entorno.nueva_variable(variable)

                            else:
                                # TODO: Error
                                pass
                        else:
                            # TODO: Error
                            pass
                    else:
                        # TODO: Error
                        pass
                else:
                    # TODO: Error
                    pass
            else:
                # TODO: Error
                pass
        else:
            # TODO: Error
            pass

        # RECURSIVO

    def obtener_dimensiones(self, valor,
                            dimensiones):  # Obtiene los tamaños de las dimensiones de un arreglo de uni/multidimensional
        if isinstance(valor, list):
            if isinstance(valor[0].valor, list):
                self.obtener_dimensiones(valor[0].valor, dimensiones)
            dimensiones.append(len(valor))

    # RECURSIVO
    def transformar(self, valor, arreglo):  # Convierte un arreglo de primitivas en un arreglo con valores normales
        if isinstance(valor, list):
            for elemento in valor:
                if isinstance(elemento.valor, list):
                    arreglo_hijo = []
                    self.transformar(elemento.valor, arreglo_hijo)
                    arreglo.append(arreglo_hijo)
                else:
                    arreglo.append(elemento.valor)

    def obtener_tipo(self, dato):  # Devuelve el tipo primitivo (si es que hay) del dato arreglo
        if isinstance(dato.valor, list):
            if len(dato.valor) > 0:
                return self.obtener_tipo(dato.valor[0])
        return dato.tipo
    # def obtener_dimensiones(dato,
    #                         dimensiones):  # Obtiene los tamaños de las dimensiones de un dato arreglo (del más exterior al más interior)
    #     if isinstance(dato.dato, list):  # el objeto tipoprimitivo.valor
    #         dimensiones.append(len(dato.dato))
    #         if len(dato.dato) > 0:
    #             obtener_dimensiones(dato.dato[0], dimensiones)
