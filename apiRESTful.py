from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL base de la API externa
BASE_URL = 'https://66eb01b755ad32cda47b4dbe.mockapi.io/loT'

# Leer todos los elementos (GET)
@app.route('/items', methods=['GET'])
def get_items():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Error al obtener los datos"}), response.status_code

# Leer un elemento por ID (GET)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    response = requests.get(f'{BASE_URL}/{item_id}')
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Elemento no encontrado"}), response.status_code

# Crear un nuevo elemento (POST)
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    response = requests.post(BASE_URL, json=new_item)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    return jsonify({"error": "Error al crear el elemento"}), response.status_code

# Actualizar un elemento por ID (PUT)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    response = requests.put(f'{BASE_URL}/{item_id}', json=updated_item)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Error al actualizar el elemento"}), response.status_code

# Eliminar un elemento por ID (DELETE)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    response = requests.delete(f'{BASE_URL}/{item_id}')
    if response.status_code == 200:
        return jsonify({"message": "Elemento eliminado exitosamente"})
    return jsonify({"error": "Error al eliminar el elemento"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
