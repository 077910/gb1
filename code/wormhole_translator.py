# Wormhole Text Converter
# Messages mutate while passing through city's infrastructure

import hashlib
from datetime import datetime

class CausalityViolation(Exception):
    pass

class MessageWormhole:
    def __init__(self):
        self.entropy_factor = int(datetime.now().timestamp()) % 256
    
    def transmit(self, message):
        original = message.encode()
        corrupted = bytearray()
        for i, b in enumerate(original):
            corrupted.append(b ^ (self.entropy_factor + i) % 256)
        
        if hash(corrupted) % 13 == 0:
            raise CausalityViolation("Message arrived before being sent")
            
        return {
            "original": message,
            "mutated": corrupted.decode(errors='replace'),
            "hash": hashlib.sha256(corrupted).hexdigest()[:8]
        }

if __name__ == "__main__":
    print("ESTABLISHING WORMHOLE COMM LINK...")
    mw = MessageWormhole()
    print(mw.transmit("The city's wiring eats messages"))