from flask import Flask, render_template, jsonify, request
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt=load('model_ml/dt1.joblib')

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
        datosEntrada = np.array([ 0.88, 0, 2.6, 0.098, 25, 67, 0.9968, 1, 0.4,
                contenido['pH'],
                contenido['sulphates'],
                contenido['alcohol']])
        # Utulizar el modelo para hacer la predicción
        resultado = dt.predict(datosEntrada.reshape(1, -1))
        # Enviar el resultado
        return jsonify({'resultado': str(resultado[0])})

# Envío de datos a través de JSON
@servidorWeb.route("/modeloForm", methods=['POST'])
def modeloForm():
        # Procesarlos datos de entrada
        contenido = request.form
        print(contenido)
        datosEntrada = np.array([ 0.88, 0, 2.6, 0.098, 25, 67, 0.9968, 1, 0.4,
                contenido['pH'],
                contenido['sulphates'],
                contenido['alcohol']])
        # Utulizar el modelo para hacer la predicción
        resultado = dt.predict(datosEntrada.reshape(1, -1))
        # Enviar el resultado
        return jsonify({'resultado': str(resultado[0])})


if __name__ == '__main__':
        servidorWeb.run(debug=False, host='0.0.0.0', port='8080')