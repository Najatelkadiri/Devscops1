from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a-very-secure-random-key')

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    
    result = cursor.fetchone()
    if result:
        return jsonify({"status": "success", "user": username})
    return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route("/compute", methods=["POST"])
def compute():
    return jsonify({"message": "This feature is disabled for security reasons"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)