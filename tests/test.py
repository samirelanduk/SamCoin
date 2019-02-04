import os
from Crypto.PublicKey import RSA
from django.test.testcases import LiveServerTestCase
from django.test.utils import override_settings
from samcoin.cryptography import PK
import samcoin

"""TEST KEY"""

SK = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDcuBqHnP4ShHIv4UgnS6Hluf/RC53STkkijudU3hmIWRn2+Poe
hSH8M8Ef+23WQvBYqBUR+kVVtBiUFNfgkvIdFyHojU1fE3Fq7mfOKZcNPsr6rXGr
WjwRi2acHocm/yCPahsZcqb7QyW48wDzwRiYV0hu/2td6+9gL0nk0fYtjwIDAQAB
AoGAIKRy+qbDheuOk6QxWUER6CQHlbFZHYw0ZrxUXAnIzuXBNZ8BfAKxJwJkcnLA
fhVCRGpUoLxZsAtwLcjzWvmAfXnPvvsqGQlSa1FAD12RoKdvvVUAjSzYkMgjwLxn
Xt8Pd1gXlPPHTzbtPdyhbXFNRsnWhX0ysqcyt8Hc62dScZkCQQDhOkQp2OuvYxBx
N0Xy5oxqYYUaEYCOLG4OpBFH5S47DUfOQXwPp+amneSNYK6J8kF7mEWHfdsofztP
DleCbZx1AkEA+uAlfKsF0fbvW/zcjNa+Kr6TYD5u/in0lzhWTvB9PYL8U6zTnHId
0r5gmTzMaUVPY6Aw+iDX4GBivI7FadyxcwJBAK2F8pY7JfoOXNCdQSsPLQeY8q9O
5LikynZFOXsmuyOL69Kg6TA2r6GW7EtwPYjSOFk8y/TDpmHhBJS3+/vk7zECQHfA
VMSMkkumNp1PNyvXOZEHxSt0weB6wHEKiFBIBVA+XRnH7n7IDipRi6S5280IM5wX
lClhUgqdl6Pv9pXQrbcCQDVzRcCovvBPQz5m6k5stdb2NJsQXtCQhQo/GvXdBiAj
m2xj2hoODakAhYNK8Yn7Kq1038+CvMiEltVnsGpJkHU=
-----END RSA PRIVATE KEY-----"""

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
        sig = samcoin.sign(message, SK)
        self.assertTrue(samcoin.verify_sign(sig, message, PK))
        self.assertFalse(samcoin.verify_sign(sig, message[:-1], PK))
        self.assertFalse(samcoin.verify_sign(sig[:-1], message[:-1], PK))
        self.assertFalse(samcoin.verify_sign(sig, message[:-1], SK))


    def test(self):
        client = samcoin.Agent(SK, PK)
        store = client.get_store(self.live_server_url)
        self.assertEqual(store.coins, [])

        client.make_coin(self.live_server_url)
        store = client.get_store(self.live_server_url)
        self.assertEqual(len(store.coins), 1)

        self.assertEqual(store.coins[0].owner, client.pk)
