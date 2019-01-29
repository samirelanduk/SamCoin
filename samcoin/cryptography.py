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

    verifier = PKCS1_v1_5.new(pk)
    digest = SHA256.new()
    digest.update(b64encode(data))
    return verifier.verify(digest, sig)
