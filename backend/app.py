from flask import Flask, request, jsonify
import json
from crypto import encrypt, decrypt

app = Flask(__name__)

PASSWORD_FILE = "passwords.json"

# Load passwords from file
def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save passwords to file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file)

@app.route("/passwords", methods=["GET"])
def get_passwords():
    encrypted_passwords = load_passwords()
    decrypted_passwords = {k: decrypt(v) for k, v in encrypted_passwords.items()}
    return jsonify(decrypted_passwords)

@app.route("/passwords", methods=["POST"])
def add_password():
    data = request.json
    if "service" in data and "password" in data:
        passwords = load_passwords()
        passwords[data["service"]] = encrypt(data["password"])
        save_passwords(passwords)
        return jsonify({"message": "Password added successfully"}), 201
    return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
