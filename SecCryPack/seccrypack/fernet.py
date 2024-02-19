from cryptography.fernet import Fernet

def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_fernet(key, plaintext):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(plaintext.encode('utf-8'))
    return ciphertext

def decrypt_fernet(key, ciphertext):
    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext).decode('utf-8')
    return plaintext
