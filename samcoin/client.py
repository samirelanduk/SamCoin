import requests
import struct
from .cryptography import sign, PK

class Agent:
    """A person"""

    def __init__(self, sk, pk):
        self.sk = sk
        self.pk = pk


    def get_store(self, url):
        r = requests.get(url)
        data = requests.get(f"{url}/store/").content
        return CoinStore(data)


    def make_coin(self, url):
        store = self.get_store(url)
        new_id = max([c.id for c in store.coins] or [-1]) + 1
        body = (new_id).to_bytes(2, byteorder="big")
        sig = sign(body, self.sk)
        b = body + sig
        response = requests.post(f"{url}/store/", data=b)
        if response.status_code != 200:
            raise Exception(response.text)



class CoinStore:

    def __init__(self, bytestring):
        chunk_num = len(bytestring) // 130
        self.coins = []
        for n in range(chunk_num):
            self.coins.append(Coin(bytestring[n * 130: n * 130 + 130]))
        for coin in self.coins:
            coin.owner = PK



class Coin:

    def __init__(self, bytestring):
        self.id = struct.unpack(">H", bytestring[:2])[0]
