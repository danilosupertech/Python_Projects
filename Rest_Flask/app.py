from flask import Flask, jsonify, request
import sqlite3

# Create the Flask application
app = Flask(__name__)

# Função utilitária para transformar tupla em dicionário


def user_to_dict(user_tuple):
    return {
        "id": user_tuple[0],
        "name": user_tuple[1],
        "email": user_tuple[2]
    }

# Endpoint para listar todos os usuários


@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    users_list = [user_to_dict(u) for u in users]
    return jsonify(users_list)

# Endpoint para listar usuário específico por ID


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify(user_to_dict(user))
    else:
        return jsonify({'message': 'User not found'}), 404

# Endpoint para criar um novo usuário


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()

    # Retorna o usuário criado completo
    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": user_id,
            "name": name,
            "email": email
        }
    }), 201

# Endpoint para atualizar um usuário existente


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "message": "User updated successfully",
        "user": {
            "id": user_id,
            "name": name,
            "email": email
        }
    })

# Endpoint para deletar um usuário


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User deleted successfully'})

# Endpoint HTML para visualizar os usuários no navegador


@app.route('/users/html', methods=['GET'])
def get_users_html():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    html = "<h1>Lista de Usuários</h1><ul>"
    for u in users:
        html += f"<li>ID: {u[0]}, Nome: {u[1]}, Email: {u[2]}</li>"
    html += "</ul>"
    return html


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)
