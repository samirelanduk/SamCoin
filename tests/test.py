from unittest import TestCase
import samcoin

class Tests(TestCase):

    def test_hashing(self):
        string = b"For in that sleep of death what dreams may come."
        hsh = samcoin.hash(string)
        self.assertEqual(len(hsh), 32)
        string2 = b"For in that sleep of death what dreams may come."
        hsh2 = samcoin.hash(string2)
        self.assertEqual(hsh, hsh2)
        string3 = b"For in that sleep of death what dreams may comeX"
        hsh3 = samcoin.hash(string3)
        self.assertNotEqual(hsh, hsh3)


    def test_block_chains(self):
        blockchain = samcoin.Blockchain()
        self.assertEqual(blockchain.data, b"")
        self.assertEqual(blockchain.items(), [])
        blockchain.append(b"GRANITA")
        self.assertEqual(blockchain.items(), [b"GRANITA"])
        self.assertEqual(blockchain.data, b"\x00\x00\x00\x00GRANITA")
