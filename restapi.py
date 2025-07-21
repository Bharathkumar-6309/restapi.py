from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store user data
users = []

# Home route
@app.route('/')
def home():
    return jsonify({"message": "User API is running"}), 200

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or not data.get('id') or not data.get('name'):
        return jsonify({"error": "Missing user ID or name"}), 400
    # Check for duplicate ID
    if any(u['id'] == data['id'] for u in users):
        return jsonify({"error": "User ID already exists"}), 400
    users.append(data)
    return jsonify({"message": "User added successfully"}), 201

# PUT - Update user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        user.update(data)
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)