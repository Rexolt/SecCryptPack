aes module
==========

This module provides functions for AES encryption and decryption.

Functions:
-----------

.. autofunction:: seccrypack.myencryption.aes.aes_encrypt

.. autofunction:: seccrypack.myencryption.aes.aes_decrypt

Examples:
---------

Encrypting and decrypting a message using AES::

   from seccrypack.myencryption import aes_encrypt, aes_decrypt

   plaintext = "Hello, AES!"
   key = b'Sixteen byte key'
   ciphertext = aes_encrypt(plaintext, key)
   decrypted_text = aes_decrypt(ciphertext, key)

   print(f"Original: {plaintext}")
   print(f"Encrypted: {ciphertext}")
   print(f"Decrypted: {decrypted_text}")

Note:
-----

The key should be a 16, 24, or 32 bytes long bytes-like object.

