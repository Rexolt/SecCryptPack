from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_keypair():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_bytes, public_key_bytes

def derive_dh_shared_key(private_key_bytes, peer_public_key_bytes):
    private_key = serialization.load_pem_private_key(private_key_bytes, backend=default_backend())
    peer_public_key = serialization.load_pem_public_key(peer_public_key_bytes, backend=default_backend())
    shared_key = private_key.exchange(peer_public_key)
    return shared_key
