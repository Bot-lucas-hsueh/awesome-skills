# python Example

```
# Authenticated classical channel using CRYSTALS-Dilithium (NIST PQC)
from cryptography.hazmat.primitives import hashes, serialization
# Use liboqs-python for post-quantum signatures
import oqs

# Bootstrap authentication with PQC signature
signer = oqs.Signature('Dilithium3')
verifier = oqs.Signature('Dilithium3')

def authenticated_send(sock, message: bytes, signing_key: bytes) -> None:
    """Send message with CRYSTALS-Dilithium signature."""
    signer_obj = oqs.Signature('Dilithium3', signing_key)
    signature = signer_obj.sign(message)
    payload = len(message).to_bytes(4, 'big') + message + signature
    sock.sendall(payload)

def authenticated_recv(sock, public_key: bytes) -> bytes:
    """Receive and verify CRYSTALS-Dilithium authenticated message."""
    msg_len = int.from_bytes(sock.recv(4), 'big')
    message = sock.recv(msg_len)
    sig_len = oqs.Signature('Dilithium3').details['length_signature']
    signature = sock.recv(sig_len)
    verifier_obj = oqs.Signature('Dilithium3')
    assert verifier_obj.verify(message, signature, public_key), \
        "Authentication FAILED — potential man-in-the-middle attack"
    return message
```
