from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode

def aes_encrypt(key, plaintext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    plaintext = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return b64encode(ciphertext)

def aes_decrypt(key, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_text = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_text) + unpadder.finalize()

    return plaintext
