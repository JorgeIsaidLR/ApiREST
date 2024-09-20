from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    message = {"greeting": "¡Hola! Bienvenido a nuestra API"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
