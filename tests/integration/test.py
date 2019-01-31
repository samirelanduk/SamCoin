import os
import samcoin
from samcoin.config import SK, PK
from Crypto.PublicKey import RSA
from unittest import TestCase

sk = RSA.importKey(SK)
pk = RSA.importKey(PK)

class Test(TestCase):

    def setUp(self):
        try:
            os.remove("teststore")
        except:
            pass
        finally:
            with open("teststore", "wb") as f: f.write(b"")
        samcoin.coins.STORE = "teststore"


    def tearDown(self):
        try:
            os.remove("teststore")
        except: pass


    def test_cryptography(self):
        message = b"for in that sleep of death what dreams may come"
        sig = samcoin.sign(message, sk)
        self.assertTrue(samcoin.verify_sign(sig, message, pk))
        self.assertFalse(samcoin.verify_sign(sig, message[:-1], pk))
        self.assertFalse(samcoin.verify_sign(sig[:-1], message[:-1], pk))
        self.assertFalse(samcoin.verify_sign(sig, message[:-1], sk))


    def test_coin_creation(self):
        person = samcoin.Agent(sk, pk)
        store = person.get_store()
        self.assertEqual(store.coins, [])

        person.create_coin()

        store = person.get_store()
        self.assertEqual(len(store.coins), 1)
        self.assertEqual(store.coins[0].id, 0)

        person.create_coin()

        store = person.get_store()
        self.assertEqual(len(store.coins), 2)
        self.assertEqual(store.coins[0].id, 0)
        self.assertEqual(store.coins[1].id, 1)
