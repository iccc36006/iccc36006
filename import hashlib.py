import hashlib
import time

class Block:
    def __init__(self, data, previous_hash='0'):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.timestamp) + self.data + self.previous_hash).encode()).hexdigest()

block = Block("Hello blockchain")
print("Block hash:", block.hash)