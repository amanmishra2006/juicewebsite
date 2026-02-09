from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

# ---------- DATABASE CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amandilkhush@904430",          # 👈 agar password hai to yaha likho
    database="login_system"
)

cursor = db.cursor(dictionary=True)

# ---------- HOME ----------
@app.route("/")
def home():
    return "Backend running 🚀"

# ---------- REGISTER ----------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "All fields required ❌"}), 400

    hashed_password = generate_password_hash(password)

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, hashed_password)
    )
    db.commit()

    return jsonify({"message": "User registered successfully ✅"})

# ---------- LOGIN ----------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user["password"], password):
        return jsonify({"message": "Login successful ✅"})
    else:
        return jsonify({"message": "Invalid email or password ❌"}), 401

# ---------- JUICES ----------
@app.route("/juices", methods=["GET"])
def juices():
    return jsonify([
        {"id": 1, "name": "Orange Juice", "price": 50},
        {"id": 2, "name": "Apple Juice", "price": 60},
        {"id": 3, "name": "Mango Juice", "price": 70}
    ])

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

