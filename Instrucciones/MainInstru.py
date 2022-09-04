from Abstracta.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from Reportes.Contenido import Errores, Tabla_Errorres, Tabla_Simbolos
from Reportes.TipoError import TIPIN_ERROR


class MainInstru(Instruccion):
    def __init__(self, fila, instruccines):
        super().__init__(fila)
        self.instrucciones = instruccines

    def ejecutar(self, entorno: Entorno):
        if self.instrucciones:
            nuevo_entorno = Entorno(entorno, entorno.flag_break, entorno.flag_return, entorno.flag_continue)
            Tabla_Simbolos.append(nuevo_entorno)
            for instruccion in self.instrucciones:
                inst = instruccion.ejecutar(entorno)
                if isinstance(inst, Break):
                    alert = "Error la instruccion Break solo puede estar dentro de un ciclo"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                elif isinstance(inst, Return):
                    alert = "Error la instruccion Return solo puede estar dentro de un ciclo"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))

                elif isinstance(inst, Continue):
                    alert = "Error la instruccion Continue solo puede estar dentro de un ciclo"
                    Tabla_Errorres.append(Errores(self.fila, alert, TIPIN_ERROR.SEMANTICO))
