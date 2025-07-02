from eth_account import Account
import secrets

acct = Account.create(secrets.token_hex(32))
message = "Hello, Recall!"
signed = Account.sign_message(message.encode(), acct.key)
print("Signed message:", signed.signature.hex())