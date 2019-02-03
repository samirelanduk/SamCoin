import os
from Crypto.PublicKey import RSA
from django.test.testcases import LiveServerTestCase
from django.test.utils import override_settings
import samcoin

"""TEST KEYS"""

SK = ("-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDcuBqHnP4ShHIv4UgnS6Hluf/" +
"RC53STkkijudU3hmIWRn2+Poe\nhSH8M8Ef+23WQvBYqBUR+kVVtBiUFNfgkvIdFyHojU1fE3Fq7mf" +
"OKZcNPsr6rXGr\nWjwRi2acHocm/yCPahsZcqb7QyW48wDzwRiYV0hu/2td6+9gL0nk0fYtjwIDAQA" +
"B\nAoGAIKRy+qbDheuOk6QxWUER6CQHlbFZHYw0ZrxUXAnIzuXBNZ8BfAKxJwJkcnLA\nfhVCRGpUo" +
"LxZsAtwLcjzWvmAfXnPvvsqGQlSa1FAD12RoKdvvVUAjSzYkMgjwLxn\nXt8Pd1gXlPPHTzbtPdyhb" +
"XFNRsnWhX0ysqcyt8Hc62dScZkCQQDhOkQp2OuvYxBx\nN0Xy5oxqYYUaEYCOLG4OpBFH5S47DUfOQ" +
"XwPp+amneSNYK6J8kF7mEWHfdsofztP\nDleCbZx1AkEA+uAlfKsF0fbvW/zcjNa+Kr6TYD5u/in0l" +
"zhWTvB9PYL8U6zTnHId\n0r5gmTzMaUVPY6Aw+iDX4GBivI7FadyxcwJBAK2F8pY7JfoOXNCdQSsPL" +
"QeY8q9O\n5LikynZFOXsmuyOL69Kg6TA2r6GW7EtwPYjSOFk8y/TDpmHhBJS3+/vk7zECQHfA\nVMS" +
"MkkumNp1PNyvXOZEHxSt0weB6wHEKiFBIBVA+XRnH7n7IDipRi6S5280IM5wX\nlClhUgqdl6Pv9pX" +
"QrbcCQDVzRcCovvBPQz5m6k5stdb2NJsQXtCQhQo/GvXdBiAj\nm2xj2hoODakAhYNK8Yn7Kq1038+" +
"CvMiEltVnsGpJkHU=\n-----END RSA PRIVATE KEY-----")

PK = ("-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcuBqH" +
"nP4ShHIv4UgnS6Hluf/R\nC53STkkijudU3hmIWRn2+PoehSH8M8Ef+23WQvBYqBUR+kVVtBiUFNfg" +
"kvIdFyHo\njU1fE3Fq7mfOKZcNPsr6rXGrWjwRi2acHocm/yCPahsZcqb7QyW48wDzwRiYV0hu\n/2" +
"td6+9gL0nk0fYtjwIDAQAB\n-----END PUBLIC KEY-----")

sk = RSA.importKey(SK)
pk = RSA.importKey(PK)

@override_settings(COIN_STORE="teststore")
class Test(LiveServerTestCase):

    def setUp(self):
        try:
            os.remove("teststore")
        except:
            pass
        finally:
            with open("teststore", "wb") as f: f.write(b"")


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


    def test(self):
        client = samcoin.Agent(sk, pk)
        store = client.get_store(self.live_server_url)
        self.assertEqual(store.coins, [])

        client.make_coin(self.live_server_url)
        store = client.get_store(self.live_server_url)
        self.assertEqual(len(store.coins), 1)
