fernet module
=============

This module provides functions for Fernet symmetric key encryption and decryption.

Functions:
-----------

.. autofunction:: seccrypack.myencryption.fernet.generate_fernet_key

.. autofunction:: seccrypack.myencryption.fernet.encrypt_fernet

.. autofunction:: seccrypack.myencryption.fernet.decrypt_fernet

Examples:
---------

Generating a Fernet key, encrypting and decrypting a message::

   from seccrypack.myencryption import fernet

   key = fernet.generate_fernet_key()

   plaintext = "Hello, Fernet!"
   ciphertext = fernet.encrypt_fernet(key, plaintext)
   decrypted_text = fernet.decrypt_fernet(key, ciphertext)

   print(f"Original: {plaintext}")
   print(f"Encrypted: {ciphertext}")
   print(f"Decrypted: {decrypted_text}")

Note:
-----

Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.

