import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/')
def index():
    return "Server oonline"

@app.route('/interpretar',methods=['post'])
def interpreptar():

    print("Se interpeeta")




@app.route('/getTablaSimbolos',methods=['post'])
def getTablaSimbolos():
    print("obtener tabla simb")



@app.route('/getTablaErrores',methods=['post'])
def getTablaErrores():
    print("get tabla errores")




app.run(port=3000, debug=True)
