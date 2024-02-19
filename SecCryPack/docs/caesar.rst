caesar module
=============

This module provides functions for Caesar cipher encryption and decryption.

Functions:
-----------

.. autofunction:: seccrypack.myencryption.caesar.caesar_cipher

Module-level Constants:
------------------------

.. autodata:: seccrypack.myencryption.caesar.ALPHABET_SIZE

Examples:
---------

Encrypting a message::

   from seccrypack.myencryption import caesar_cipher

   plaintext = "Hello, Caesar!"
   shift = 3
   ciphertext = caesar_cipher(plaintext, shift)
   print(f"Encrypted: {ciphertext}")

Decrypting a message::

   from seccrypack.myencryption import caesar_cipher

   ciphertext = "Khoor, Fdhvdu!"
   shift = 3
   decrypted_text = caesar_cipher(ciphertext, -shift)
   print(f"Decrypted: {decrypted_text}")

