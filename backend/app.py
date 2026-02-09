from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TEMP USERS (instead of MySQL)
users = [
    {"email": "test@gmail.com", "password": "1234"}
]

@app.route("/")
def home():
    return "Juice Backend Running 🚀"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({"message": "Login successful ✅"})

    return jsonify({"message": "Login failed ❌"}), 401


@app.route("/juices", methods=["GET"])
def juices():
    return jsonify([
        {"id": 1, "name": "Orange Juice", "price": 50},
        {"id": 2, "name": "Apple Juice", "price": 60},
        {"id": 3, "name": "Mango Juice", "price": 70}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
