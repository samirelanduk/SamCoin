from coins import *
from Crypto.PublicKey import RSA

store = CoinStore("coins.cs")

key = RSA.generate(1024)
agent = Agent(key.exportKey(), key.publickey().exportKey())

coin = agent.create_coin(store)
