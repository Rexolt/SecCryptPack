diffie_hellman module
=====================

This module provides functions for Diffie-Hellman key exchange.

Functions:
-----------

.. autofunction:: seccrypack.myencryption.diffie_hellman.generate_dh_keypair

.. autofunction:: seccrypack.myencryption.diffie_hellman.derive_dh_shared_key

Examples:
---------

Generating Diffie-Hellman key pairs and deriving shared keys::

   from seccrypack.myencryption import diffie_hellman

   # Alice's key pair
   alice_private, alice_public = diffie_hellman.generate_dh_keypair()

   # Bob's key pair
   bob_private, bob_public = diffie_hellman.generate_dh_keypair()

   # Alice derives shared key
   shared_key_alice = diffie_hellman.derive_dh_shared_key(alice_private, bob_public)

   # Bob derives shared key
   shared_key_bob = diffie_hellman.derive_dh_shared_key(bob_private, alice_public)

   print(f"Alice's shared key: {shared_key_alice}")
   print(f"Bob's shared key: {shared_key_bob}")

Note:
-----

Diffie-Hellman key exchange allows two parties to establish a shared secret over an insecure channel.

