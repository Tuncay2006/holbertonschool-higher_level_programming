from flask import Flask, jsonify, request

app = Flask(__name__)

# Kullanıcı verilerini bellekte tutuyoruz
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    # Tüm kullanıcı isimlerini liste olarak döndürür
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Yeni kullanıcı objesi oluşturuyoruz
    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run()
