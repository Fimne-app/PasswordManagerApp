# Password Manager Application

## Overview

This is a Password Manager application designed to securely store and retrieve passwords. It consists of two main components:

1. **Backend (Python)**: A Flask-based API for managing passwords. Passwords are securely encrypted using the `cryptography` library.
2. **Frontend (Java)**: A console-based application that interacts with the backend to add and retrieve passwords.

---

## Features

### Backend
- **Flask API**:
  - `GET /passwords`: Retrieves all stored passwords (decrypted).
  - `POST /passwords`: Adds a new password for a specific service (encrypts before saving).
- **Encryption**:
  - Passwords are encrypted using `cryptography.fernet` to ensure security.

### Frontend
- **Console-based Java Application**:
  - View stored passwords by interacting with the Flask API.
  - Add new passwords by sending POST requests to the Flask API.

---

## Installation

### Prerequisites
1. Python 3.9+
2. Java 11+
3. pip (Python package manager)

### Backend Setup
1. Navigate to the `backend` directory.
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Compile the Java code:
   ```bash
   javac *.java
   ```
3. Run the application:
   ```bash
   java Main
   ```

---

## File Structure

```
PasswordManagerApp/
├── backend/
│   ├── app.py               # Flask application
│   ├── crypto.py            # Encryption and decryption utilities
│   ├── passwords.json       # Stores encrypted passwords
│   ├── requirements.txt     # Python dependencies
├── frontend/
│   ├── Main.java            # Entry point for the Java application
│   ├── PasswordManager.java # Logic for the console-based manager
│   ├── APIClient.java       # Handles API interactions
```

---

## How It Works

### Backend
1. Passwords are stored in a `passwords.json` file in an encrypted format.
2. The `crypto.py` module uses `cryptography.fernet` for encryption and decryption.

### Frontend
1. Users interact with the Java console application.
2. The `APIClient` sends HTTP requests to the Flask API for data retrieval and storage.

---

## Future Enhancements
- Add a GUI for the frontend application.
- Implement user authentication for enhanced security.
- Store encryption keys securely (e.g., environment variables or secure vaults).

---

## License

This project is open-source and available under the MIT License.
