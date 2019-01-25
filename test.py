from coins import *
from Crypto.PublicKey import RSA
from unittest import TestCase

class Test(TestCase):

    def test(self):
        store = CoinStore("coins.cs")
        self.assertEqual(store.coins, [])

        key = RSA.generate(1024)
        agent = Agent(key.exportKey(), key.publickey().exportKey())

        coin = agent.create_coin(store)
        self.assertEqual(store.coins, [coin])
