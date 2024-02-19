# 🛡️ SecCryPack

SecCryPack is a Python package providing a comprehensive collection of encryption methods for secure communication. Whether you're a security enthusiast or a developer looking to implement robust encryption in your applications, SecCryPack has you covered.

## 🌟 Features

- **Caesar Cipher**: A simple substitution cipher used for educational purposes and basic encryption needs.
- **AES Encryption/Decryption**: The Advanced Encryption Standard for symmetric key encryption, ensuring strong security.
- **RSA Key Generation, Encryption, and Decryption**: Asymmetric key algorithm for secure communication and digital signatures.
- **Fernet Symmetric Key Encryption/Decryption**: A lightweight and secure method for symmetric encryption.
- **Diffie-Hellman Key Exchange**: A secure key exchange protocol for establishing shared secrets over an insecure communication channel.

## 🚀 Installation

```bash
pip install seccrypack
```
## 📚Usage
```bash
from seccrypack.myencryption import caesar_cipher, aes_encrypt, aes_decrypt, generate_rsa_keypair
from seccrypack.myencryption.fernet import generate_fernet_key, encrypt_fernet, decrypt_fernet
from seccrypack.myencryption.diffie_hellman import generate_dh_keypair, derive_dh_shared_key

# Example: Caesar cipher
plaintext = "Hello, SecCryPack!"
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print(f"Caesar Cipher: {ciphertext}")

# Example: AES encryption/decryption
key = b'Sixteen byte key'
encrypted_text = aes_encrypt(plaintext, key)
decrypted_text = aes_decrypt(encrypted_text, key)
print(f"AES Encrypted: {encrypted_text}")
print(f"AES Decrypted: {decrypted_text}")

# Example: RSA key generation, encryption, and decryption
private_key, public_key = generate_rsa_keypair()
rsa_encrypted_text = encrypt_rsa(public_key, plaintext)
rsa_decrypted_text = decrypt_rsa(private_key, rsa_encrypted_text)
print(f"RSA Encrypted: {rsa_encrypted_text}")
print(f"RSA Decrypted: {rsa_decrypted_text}")

# Example: Fernet symmetric key encryption/decryption
fernet_key = generate_fernet_key()
fernet_encrypted_text = encrypt_fernet(fernet_key, plaintext)
fernet_decrypted_text = decrypt_fernet(fernet_key, fernet_encrypted_text)
print(f"Fernet Encrypted: {fernet_encrypted_text}")
print(f"Fernet Decrypted: {fernet_decrypted_text}")

# Example: Diffie-Hellman key exchange
alice_private, alice_public = generate_dh_keypair()
bob_private, bob_public = generate_dh_keypair()

shared_key_alice = derive_dh_shared_key(alice_private, bob_public)
shared_key_bob = derive_dh_shared_key(bob_private, alice_public)

print(f"Alice's shared key: {shared_key_alice}")
print(f"Bob's shared key: {shared_key_bob}")

```

# 🤝Contributing

Contributions are welcome! Feel free to open issues or pull requests.
