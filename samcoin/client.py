import requests

class Agent:
    """A person"""

    def __init__(self, sk, pk):
        self.sk = sk
        self.pk = pk


    def get_store(self, url):
        data = requests.get(f"{url}/store/")
        return CoinStore(data)



class CoinStore:

    def __init__(self, bytestring):
        chunk_num = len(bytestring) // 130
        self.coins = []
        for n in range(chunk_num):
            self.coins.append(Coin(bytestring[n * 130: n * 130 + 130]))



class Coin:

    def __init__(self, bytestring):
        self.id = struct.unpack(">H", bytestring[:2])[0]
