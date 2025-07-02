from web3 import Web3
from eth_account import Account

account = Account.create()
print("Address:", account.address)
print("Private Key:", account.privateKey.hex())