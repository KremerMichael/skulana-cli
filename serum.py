import solana
import base64
from solana.rpc.api import Client
#import pyserum

# transaction is collection of instructions
# sign transaction & serialize into wire formatd
# send_raw_transaction w/ api client or async api client

LAMPORTS_PER_SOL = 1000000000


# First we need a client to even connect to solana-rpc

BTC_USDC="A8YFbxQYFVqKZaoYJLLUVcQiWP7G2MeEgW5wsAQgMvFw"


# using phantom api
sol_clients = {"phantom_mainnet":"https://solana-mainnet.phantom.tech",
               "testnet": "https://api.testnet.solana.com",
               "devnet": "https://api.devnet.solana.com"}

rhom_pubkey="Fhhq7AtgMsWge7oBMMWkqaF4boMLJ6Utcmc2X1oEsqJQ"

sol_client = Client(sol_clients["phantom_mainnet"])


print(sol_client.get_balance(rhom_pubkey))
balance = sol_client.get_balance(rhom_pubkey)
print(balance['result']['value'])
print(balance['result']['value']/LAMPORTS_PER_SOL)
print()
print()

print(sol_client.get_account_info(BTC_USDC))
mkt_info = sol_client.get_account_info(BTC_USDC)

data = mkt_info["result"]["value"]["data"][0]
_bytes = base64.decodebytes(data.encode("ascii"))


print()
print(_bytes)
print()
print(len(_bytes))

# This is a bit hacky at the moment. The first 5 bytes are padding, the
# total length is 8 bytes which is 5 + 8 = 13 bytes.

print(type(_bytes))

name = _bytes[0:5]
account_flags = _bytes[5:13]
slab = _bytes[13:]

#print(f"name: {name}\naccount_flags: {account_flags}\nslab: {slab}")






