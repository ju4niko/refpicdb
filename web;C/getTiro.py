#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        data = request.get_json()  # Accede a los datos JSON
        valor1 = data.get('valor1')
        valor2 = data.get('valor2')
        valor3 = data.get('valor3')
        posicionGPS = data.get('posicionGPS')

        print(f'Valor 1:{valor1}')
        print(f'Valor 2:{valor2}')
        print(f'Valor 3:{valor3}')
        print(f'Posición GPS:{posicionGPS}')

        return "Recibido" 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=15000, debug=True)

