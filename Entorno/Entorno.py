from Entorno.Variable import Variable

class Entorno:
    def __int__(self, padre, tipo):
        self.padre = padre #! Entorno principal
        self.tipo = tipo
        self.tabla_variables = {} #? Tabla solo para variables
        self.tabla_funcion = {} #? Tabla solo para funciones
        self.tabla_struct = {} #? Tabla solo para struct

    def nueva_variable(self, variable: Variable):
        self.tabla_variables[variable.nombre] = variable
