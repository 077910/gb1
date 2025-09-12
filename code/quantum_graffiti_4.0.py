# Quantum Graffiti 4.0
# Tags every possible quantum branch with schrodinger's spraycan

import random
from enum import Enum

class ParadoxState(Enum):
    OBSERVED = "Collapsed into cringe"
    SUPERPOSED = "Dank in 5 dimensions"
    ENTANGLED = "Your mom's blockchain"

class MultiverseArtist:
    def __init__(self):
        self.tag_db = [
            "THIS MEMORY LEAK GENTRIFIES",
            "YOUR POINTER IS IN ANOTHER CASTLE",
            "SEGFAULT WAS AN INSIDE JOB"
        ]
    
    def quantum_tag(self):
        state = random.choice(list(ParadoxState))
        return f"[{random.choice(self.tag_db)}] | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM")
    artist = MultiverseArtist()
    print(artist.quantum_tag())