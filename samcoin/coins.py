class Agent:
    """A person"""

    def __init__(self, sk, pk):
        self.sk = sk
        self.pk = pk


    def create_coin(self, store):
        coin = Coin()
        store.coins.append(coin)
        return coin



class CoinStore:

    def __init__(self, path):
        self.coins = []



class Coin:

    def __init__(self, id):
        self.id = id
