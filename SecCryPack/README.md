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

## 📄 License



SecCryPack is open-source and released under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.


© 2024 Rexolt

**Disclaimer:**

The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.