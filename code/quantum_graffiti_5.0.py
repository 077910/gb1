# Quantum Graffiti 5.0
# Tags across Hilbert space with meme magic

from enum import Enum
import random
import hashlib

class MemeField(Enum):
    SCHRODINGER = "Simultaneously based and cringe"
    HEISENBERG = "Can't measure position without disturbing the lulz"
    EINSTEIN = "Relatively autistic"

class QuantumVandal:
    def __init__(self):
        self.canvas = [
            "0xDEADBEEF was here",
            "This memory address gentrified",
            "Segmentation fault (core dumped into your DMs)"
        ]
        
    def tag(self, observer):
        state = random.choice(list(MemeField))
        art = random.choice(self.canvas)
        sig = hashlib.md5((art + observer).encode()).hexdigest()
        return f"{art} | STATE: {state.value} | OBSERVER: {sig[:6]}"

if __name__ == "__main__":
    print("SPRAYING HILBERT SPACE...")
    qv = QuantumVandal()
    print(qv.tag("Gatsu"))