# Quantum Graffiti 8.0
# Now spraying in 11 dimensions

from enum import Enum
import random
import numpy as np

class HyperSpray(Enum):
    TACHYON = "Tags before you see them"
    NONLOCAL = "Simultaneously on all walls"
    ENTANGLED = "Changes when observed"

class StreetArtCollider:
    def __init__(self):
        self.quotes = [
            "YOUR MEMORY LEAK HAS GENTRIFIED",
            "THIS FUNCTION IS A TUNNEL TO BERLIN",
            "STACK OVERFLOW = MODERN KOAN"
        ]
        self.dimensions = 11
    
    def tag(self):
        coords = [random.gauss(0,1) for _ in range(self.dimensions)]
        style = random.choice(list(HyperSpray))
        return f"[{np.linalg.norm(coords):.2f}D] {random.choice(self.quotes)} | {style.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM PROTOCOL")
    vandal = StreetArtCollider()
    print(vandal.tag())