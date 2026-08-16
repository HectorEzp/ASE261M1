from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista temporal de clientes
clientes = []
contador_id = 1


# Página principal
@app.route('/')
def index():
    return render_template('index.html')


# Página de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


# GET - Listar clientes
@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    return jsonify(clientes)


# POST - Agregar cliente
@app.route('/api/clientes', methods=['POST'])
def agregar_cliente():
    global contador_id

    datos = request.get_json()

    nombre = datos.get('nombre')
    email = datos.get('email')

    if not nombre or not email:
        return jsonify({
            'mensaje': 'Nombre y email son obligatorios'
        }), 400

    nuevo_cliente = {
        'id': contador_id,
        'nombre': nombre,
        'email': email
    }

    clientes.append(nuevo_cliente)
    contador_id += 1

    return jsonify(nuevo_cliente), 201


# PUT - Actualizar cliente
@app.route('/api/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    datos = request.get_json()

    for cliente in clientes:
        if cliente['id'] == id:

            cliente['nombre'] = datos.get('nombre')
            cliente['email'] = datos.get('email')

            return jsonify(cliente)

    return jsonify({
        'mensaje': 'Cliente no encontrado'
    }), 404


# DELETE - Eliminar cliente
@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):

    for cliente in clientes:
        if cliente['id'] == id:

            clientes.remove(cliente)

            return jsonify({
                'mensaje': 'Cliente eliminado correctamente'
            })

    return jsonify({
        'mensaje': 'Cliente no encontrado'
    }), 404


# Ejecutar aplicación
if __name__ == '__main__':
    app.run(debug=True)