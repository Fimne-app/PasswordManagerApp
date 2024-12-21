from cryptography.fernet import Fernet

# Key for encryption (replace with a securely stored key in production)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def encrypt(password):
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()
