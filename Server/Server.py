import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route('/')
def index():
    return "Server oonline"


@app.route('/interpretar', methods=['post'])
def interpretar():
    if request.method == 'POST':
        print(request.json)
        return jsonify(
            {"estado": "200",
             })


@app.route('/getTablaSimbolos', methods=['post'])
def getTablaSimbolos():
    print("obtener tabla simb")


@app.route('/getTablaErrores', methods=['post'])
def getTablaErrores():
    print("get tabla errores")


if __name__ == '__main__':
    app.run(port=7000, debug=True, host='localhost')
