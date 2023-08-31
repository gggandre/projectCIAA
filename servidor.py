from flask import Flask, render_template, jsonify, request
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt=load('dt1.joblib')

# Generar el servidor (Backend)
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo", methods=['GET'])
def holamundo():
        return render_template('pagina1.html')

# Envío de datos a través de JSON
@servidorWeb.route("/modelo", methods=['POST'])
def modeloPrediccion():
        # Procesarlos datos de entrada
        contenido = request.json
        print(contenido)
        return jsonify({'resultado': "Hola"})

if __name__ == '__main__':
        servidorWeb.run(debug=False, host='0.0.0.0', port='8080')