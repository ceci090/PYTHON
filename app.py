from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET simple
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({"mensaje": "¡Hola desde tu API en Python!"})

# Ruta POST que recibe JSON y suma dos números
@app.route('/sumar', methods=['POST'])
def sumar():
    datos = request.get_json()
    a = datos.get('a')
    b = datos.get('b')
    
    if a is None or b is None:
        return jsonify({"error": "Faltan parámetros 'a' y 'b'"}), 400

    resultado = a + b
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
