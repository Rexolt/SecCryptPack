rsa module
==========

This module provides functions for RSA key generation, encryption, and decryption.

Functions:
-----------

.. autofunction:: seccrypack.myencryption.rsa.generate_rsa_keypair

.. autofunction:: seccrypack.myencryption.rsa.encrypt_rsa

.. autofunction:: seccrypack.myencryption.rsa.decrypt_rsa

Examples:
---------

Generating an RSA key pair, encrypting and decrypting a message::

   from seccrypack.myencryption import generate_rsa_keypair, encrypt_rsa, decrypt_rsa

   private_key, public_key = generate_rsa_keypair()

   plaintext = "Hello, RSA!"
   ciphertext = encrypt_rsa(public_key, plaintext)
   decrypted_text = decrypt_rsa(private_key, ciphertext)

   print(f"Original: {plaintext}")
   print(f"Encrypted: {ciphertext}")
   print(f"Decrypted: {decrypted_text}")

Note:
-----

The RSA key pair generation may take some time due to the complexity of the algorithm.

