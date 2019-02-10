"""Cryptographic utilities."""

from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def sign(data, sk):
    """Signs some data.

    :param bytes data: the message to sign.
    :param RsaKey sk: the private key to sign with.
    :rtype: ``bytes``"""

    sk = RSA.importKey(sk)
    digest = SHA256.new()
    digest.update(b64encode(data))
    signer = PKCS1_v1_5.new(sk)
    sig = signer.sign(digest)
    return sig


def verify_sign(sig, data, pk):
    """Checks that a signature on a document matches the document and a public
    key.

    :param bytes sig: the signature to check.
    :param bytes data: the message to check.
    :param RsaKey pk: the public key check.
    :rtype: ``bool``"""

    pk = RSA.importKey(pk)
    verifier = PKCS1_v1_5.new(pk)
    digest = SHA256.new()
    digest.update(b64encode(data))
    return verifier.verify(digest, sig)


def hash(data):
    return SHA256.new(data=data).digest()


PK = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcuBqHnP4ShHIv4UgnS6Hluf/R
C53STkkijudU3hmIWRn2+PoehSH8M8Ef+23WQvBYqBUR+kVVtBiUFNfgkvIdFyHo
jU1fE3Fq7mfOKZcNPsr6rXGrWjwRi2acHocm/yCPahsZcqb7QyW48wDzwRiYV0hu
/2td6+9gL0nk0fYtjwIDAQAB
-----END PUBLIC KEY-----"""
