from flask import Flask, jsonify, request
import sqlite3

# Create the Flask application
app = Flask(__name__)


def user_to_dict(user_tuple):
    """
    Convert a SQLite row (tuple) into a Python dictionary.

    Args:
        user_tuple (tuple): A tuple representing a user record 
                            in the format (id, name, email).

    Returns:
        dict: A dictionary with keys "id", "name", and "email".
    """
    return {
        "id": user_tuple[0],
        "name": user_tuple[1],
        "email": user_tuple[2]
    }


@app.route('/users', methods=['GET'])
def get_users():
    """
    GET /users
    Retrieve all users from the database.

    Returns:
        JSON: A list of users in JSON format.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    users_list = [user_to_dict(u) for u in users]
    return jsonify(users_list)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    GET /users/<user_id>
    Retrieve a specific user by ID.

    Args:
        user_id (int): ID of the user to retrieve.

    Returns:
        JSON: User data if found, otherwise 404 error message.
    """
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


@app.route('/users', methods=['POST'])
def create_user():
    """
    POST /users
    Create a new user with name and email.

    Request body (JSON):
        {
            "name": "User Name",
            "email": "user@email.com"
        }

    Returns:
        JSON: Message and the created user object with ID.
    """
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

    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": user_id,
            "name": name,
            "email": email
        }
    }), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    PUT /users/<user_id>
    Update an existing user's name and email.

    Args:
        user_id (int): ID of the user to update.

    Request body (JSON):
        {
            "name": "Updated Name",
            "email": "updated@email.com"
        }

    Returns:
        JSON: Message and updated user data.
    """
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


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    DELETE /users/<user_id>
    Delete a user by ID.

    Args:
        user_id (int): ID of the user to delete.

    Returns:
        JSON: Confirmation message after deletion.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User deleted successfully'})


@app.route('/users/html', methods=['GET'])
def get_users_html():
    """
    GET /users/html
    Retrieve all users and display them in a simple HTML format.

    Returns:
        str: An HTML unordered list of users.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    html = "<h1>User List</h1><ul>"
    for u in users:
        html += f"<li>ID: {u[0]}, Name: {u[1]}, Email: {u[2]}</li>"
    html += "</ul>"
    return html


if __name__ == '__main__':
    # Run the application in debug mode on localhost, port 5500
    app.run(debug=True, host='127.0.0.1', port=5500)
