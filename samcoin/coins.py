import struct
from .cryptography import sign
from .config import STORE, SK, PK

class Agent:
    """A person"""

    def __init__(self, sk, pk):
        self.sk = sk
        self.pk = pk
        self.manager = self.sk.exportKey() == SK.encode()



    def get_store(self):
        with open(STORE, "rb") as f:
            return CoinStore(f.read())


    def create_coin(self):
        store = self.get_store()
        new_id = max([c.id for c in store.coins] or [-1]) + 1
        body = (new_id).to_bytes(2, byteorder="big")
        sig = sign(body, self.sk)
        b = body + sig
        with open(STORE, "ab") as f:
            f.write(b)



class CoinStore:

    def __init__(self, bytestring):
        chunk_num = len(bytestring) // 130
        self.coins = []
        for n in range(chunk_num):
            self.coins.append(Coin(bytestring[n * 130: n * 130 + 130]))



class Coin:

    def __init__(self, bytestring):
        self.id = struct.unpack(">H", bytestring[:2])[0]
