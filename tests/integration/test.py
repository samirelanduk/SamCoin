import samcoin
from Crypto.PublicKey import RSA
from unittest import TestCase

class Test(TestCase):

    def test_cryptography(self):
        sk = RSA.generate(1024)
        print(type(sk))
        pk = sk.publickey()
        message = b"for in that sleep of death what dreams may come"
        sig = samcoin.sign(message, sk)
        self.assertTrue(samcoin.verify_sign(sig, message, pk))
        self.assertFalse(samcoin.verify_sign(sig, message[:-1], pk))
        self.assertFalse(samcoin.verify_sign(sig[:-1], message[:-1], pk))
        self.assertFalse(samcoin.verify_sign(sig, message[:-1], sk))
