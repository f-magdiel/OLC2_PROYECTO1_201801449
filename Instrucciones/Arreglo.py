from Abstracta.Instruccion import Instruccion
from Enumeradas.Primitivo import tipoPrimitivo
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva


class Arreglo(Instruccion):
    def __init__(self, fila, expresiones):
        super().__init__(fila)
        self.expresiones = expresiones

    def ejecutar(self, entorno: Entorno):
        aux = []

        # Validar que venga al menos una expresión (NO [])
        if self.expresiones:
            # Recorrer e interpretar las expresiones
            for i in range(len(self.expresiones)):
                aux.append(self.expresiones[i].ejecutar(entorno))
            # Validar que ninguna primitiva sea None
            if None not in aux:
                # Obtener el tipo del primer elemento para determinar el resultante
                tipo = aux[0].tipo
                # Recorrer las primitivas y verificar el tipo
                correctas = True
                for primitiva in aux:
                    if primitiva.tipo != tipo:
                        correctas = False
                        break
                # Validar que sean del mismo tipo
                if correctas:
                    # Recorrer las primitivas y verificar si al menos una primitiva es un arreglo, si es asi, capturar el tamaño
                    es_arreglo = False
                    tamanyo = 0
                    for primitiva in aux:
                        if isinstance(primitiva.valor, list):
                            tamanyo = len(primitiva.valor)
                            es_arreglo = True
                            break
                    # Validar si deberían ser arreglos
                    if not es_arreglo:
                        # Retornar una nueva primitiva con el tipo y valor del arreglo de expresiones procesado
                        return Primitiva(self.fila, tipoPrimitivo.ARREGLO, aux)
                    else:
                        # Recorrer las primitivas y verificar si sus valores son listas y tienen el mismo tamaño
                        correctas = True
                        for primitiva in aux:
                            if not isinstance(primitiva.valor, list) or len(primitiva.valor) != tamanyo:
                                correctas = False
                                break
                        # Validar si todas las primitivas tienen el mismo tamaño en sus valores
                        if correctas:
                            # Retornar una nueva primitiva con el tipo y valor del arreglo de expresiones procesado
                            return Primitiva(self.fila,  tipoPrimitivo.ARREGLO, aux)
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