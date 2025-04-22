from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de usuarios (almacenada en memoria)
usuarios = []

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    info_data = {
        "system": "Servidor Flask para la gestión de usuarios",
        "version": "1.0",
        "author": "Noel"
    }
    return jsonify(info_data)

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()  # Obtener los datos JSON enviados en el POST
    
    # Validar si los datos necesarios están presentes
    if 'nombre' not in data or 'correo' not in data:
        return jsonify({"error": "Faltan datos: nombre y correo son obligatorios"}), 400
    
    # Añadir el nuevo usuario a la lista
    usuario = {
        "nombre": data['nombre'],
        "correo": data['correo']
    }
    usuarios.append(usuario)
    
    return jsonify({"message": "Usuario creado con éxito", "usuario": usuario}), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == '__main__':
    app.run(debug=True)
