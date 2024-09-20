from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta que acepta GET y muestra un saludo
@app.route('/greet', methods=['GET'])
def greet_get():
    return jsonify({"message": "Llamaste al método GET en la ruta /greet"})

# Ruta que acepta POST y confirma recepción de datos
@app.route('/greet', methods=['POST'])
def greet_post():
    data = request.get_json()
    return jsonify({"message": "Llamaste al método POST en la ruta /greet", "data_received": data})

# Ruta que acepta PUT y muestra que se está actualizando algo
@app.route('/greet', methods=['PUT'])
def greet_put():
    data = request.get_json()
    return jsonify({"message": "Llamaste al método PUT en la ruta /greet", "data_updated": data})

# Ruta que acepta DELETE y muestra que se está eliminando algo
@app.route('/greet', methods=['DELETE'])
def greet_delete():
    return jsonify({"message": "Llamaste al método DELETE en la ruta /greet"})

if __name__ == '__main__':
    app.run(debug=True)
