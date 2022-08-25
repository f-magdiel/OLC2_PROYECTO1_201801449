from Entorno.Variable import Variable


class Entorno:
    def __init__(self, padre, flag_break, flag_return, flag_continue):
        self.padre = padre  # ! Entorno principal
        self.flag_break = flag_break
        self.flag_return = flag_return
        self.flag_continue = flag_continue
        self.tabla_variables = {}  # ? Tabla solo para variables
        self.tabla_funcion = {}  # ? Tabla solo para funciones
        self.tabla_struct = {}  # ? Tabla solo para struct

    def nueva_variable(self, variable: Variable):
        self.tabla_variables[variable.nombre] = variable

    def editar_variable(self, nombre, nueva: Variable):
        entorno_actual = self
        while (entorno_actual):
            var = entorno_actual.tabla_variables.get(nombre)
            if (var):
                entorno_actual.tabla_variables[nombre] = nueva
                return True
            entorno_actual = entorno_actual.padre
        return False

    def buscar_variable(self, nombre):
        entorno_actual = self
        while (entorno_actual):
            var = entorno_actual.tabla_variables.get(nombre)
            if (var):
                return var
            entorno_actual = entorno_actual.padre
        return None

    def buscar_variable_entorno(self, nombre):
        var = self.tabla_variables.get(nombre)
        if (var):
            return True

        return False
