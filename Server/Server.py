import json
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from Analizador.Sintactico import parser
from Reportes.Contenido import Tabla_Errorres, Tabla_Simbolos, Errores, Tabla_Impresion
from Entorno.Entorno import Entorno
from Instrucciones.MainInstru import MainInstru
from Funciones.Funciones import Funciones
from Reportes.TipoError import TIPIN_ERROR

lista_variables = []
lista_funciones = []
lista_errores = []

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route('/')
def index():
    return "Server oonline"


@app.route('/interpretar', methods=['post'])
def interpretar():
    if request.method == 'POST':
        # ! Se manda al expresion
        entradas = request.json["code"]
        print(entradas)
        cadena_impresion = ""
        str_entradas = str(entradas)

        instr = parser.parse(str_entradas)
        entorno_global = Entorno(None, None, None, None)
        if instr:
            for isn in instr:
                if isinstance(isn, MainInstru):
                    isn.ejecutar(entorno_global)
                elif isinstance(isn, Funciones):
                    isn.ejecutar(entorno_global)

        else:
            alert = "Error al ejecutar instrucciones del analizador"
            Tabla_Errorres.append(Errores(0, alert, TIPIN_ERROR.SEMANTICO))

        # ! Para concatenar instruccines
        for ins1 in Tabla_Impresion:
            cadena_impresion += ins1 + "\n"

        # ! para recorrer tabla de simbolos y funcines

        for entorno1 in Tabla_Simbolos:
            for i in entorno1.tabla_variables:
                lista = [str(entorno1.tabla_variables[i].nombre), str(entorno1.tabla_variables[i].valor), str(entorno1.tabla_variables[i].tipo), str(entorno1.tabla_variables[i].linea)]
                lista_variables.append(lista)

            for j in entorno1.tabla_funciones:
                lista_funs = ""
                for k in entorno1.tabla_funciones[j].parametros:
                    lista_funs += k.nombre + " \n"

                lista = [str(entorno1.tabla_funciones[j].nombre), str(lista_funs), str(entorno1.tabla_funciones[j].tipo), str(entorno1.tabla_funciones[j].linea)]
                lista_variables.append(lista)

        # ! para errores
        if len(Tabla_Errorres) > 0:
            for err in Tabla_Errorres:
                _errores = [str(err.fila), str(err.tipo), str(err.info), str(err.tiempo)]
                lista_errores.append(_errores)
        else:
            _errores = ["", "", "", ""]
            lista_errores.append(_errores)

        # ! se manda para el front
        res = jsonify({
            'consola': cadena_impresion
        })
        cadena_impresion=""
        return res


@app.route('/getTablaSimbolos', methods=['post'])
def getTablaSimbolos():
    print("obtener tabla simb")


@app.route('/getTablaErrores', methods=['post'])
def getTablaErrores():
    print("get tabla errores")


if __name__ == '__main__':
    app.run(port=7000, debug=True, host='localhost')
