from Abstracta.Instruccion import Instruccion
from Entorno.Variable import Variable
from Entorno.Entorno import Entorno
from Expresiones.Primitiva import Primitiva
from Enumeradas.NativeVectores import NATIVE_VECTORES
from Enumeradas.Primitivo import tipoPrimitivo
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores
from Reportes.TipoError import TIPIN_ERROR


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
            var = entorno.buscar_variable(self.id.nombre)
            if var:
                return Primitiva(self.fila, tipoPrimitivo.I64, var.capacidad)
            else:
                alert = "Error no se puede aplicar CAPACITY a esta expresion"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

        elif NATIVE_VECTORES.PUSH == self.funcion:


            var = entorno.buscar_variable(self.id.nombre)
            data = self.expresion1.ejecutar(entorno)
            if data:
                if var and type(var.valor) is list:
                    var.valor.append(data)
                    entorno.editar_variable(self.id.nombre, var)
                else:
                    alert = "Error no se puede aplicar PUSH a esta expresion"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)


        elif NATIVE_VECTORES.CONTAINS == self.funcion:
            if hasattr(self.id, 'nombre'):
                flag_contain = False
                var = entorno.buscar_variable(self.id.nombre)
                buscar = self.expresion1.valor

                if var:
                    for i in var.valor:
                        auxi = i.valor

                        if auxi == buscar:
                            flag_contain = True
                            break
                else:
                    alert = "Error expresion invalido para aplicar CONTAINS"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)

                if flag_contain:
                    return Primitiva(self.fila, tipoPrimitivo.BOOL, True)
                else:
                    return Primitiva(self.fila, tipoPrimitivo.BOOL, False)
            else:
                alert = "Error expresion invalido para aplicar CONTAINS"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)


        elif NATIVE_VECTORES.REMOVE == self.funcion:

            var = entorno.buscar_variable(self.id.nombre)
            pos = self.expresion1.ejecutar(entorno)

            if pos.valor < len(var.valor):
                var.valor.pop(pos.valor)
                entorno.editar_variable(self.id.nombre, var)

            else:
                alert = "Error expresion invalido para aplicar REMOVE"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)


        elif NATIVE_VECTORES.REMOVE_EXPRE == self.funcion:
            if hasattr(self.id, 'nombre'):
                var = entorno.buscar_variable(self.id.nombre)
                pos = self.expresion1.ejecutar(entorno)
                if hasattr(var, 'valor'):

                    if pos.valor < len(var.valor):
                        newvariable = var.valor.pop(pos.valor)
                        entorno.editar_variable(self.id.nombre, var)
                        return Primitiva(self.fila, pos.tipo, newvariable.valor)
                    else:
                        alert = "Error indice fuera de rango"
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)
                else:
                    alert = "Error expresion invalido para aplicar REMOVE"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                    print(alert)

            else:
                alert = "Error expresion invalido para aplicar REMOVE"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

        elif NATIVE_VECTORES.INSERT == self.funcion:
            if hasattr(self.id, 'nombre'):
                var = entorno.buscar_variable(self.id.nombre)
                data = self.expresion2.ejecutar(entorno)
                pos = self.expresion1.ejecutar(entorno)
                if data and pos:
                    if hasattr(var, 'valor'):
                        if pos.valor <= len(var.valor):
                            var.valor.insert(pos.valor, data)
                            entorno.editar_variable(self.id.nombre, var)
                        else:
                            alert = "Error indice fuera del rango"
                            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                            print(alert)
                    else:
                        alert = "Error expresion invalido para aplicar INSERT"
                        Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                        print(alert)
            else:
                alert = "Error expresion invalido para aplicar INSERT"
                Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
                print(alert)

        else:
            alert = "Error el tipo de la funcion nativa no existe"
            Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
            print(alert)
