# Quantum Banksy 16.0
# Tags spacetime itself

import random
from enum import Enum

class Dimension(Enum):
    HOLOGRAM = "Tag persists across 11 dimensions"
    EIGENSTATE = "Only visible when not observed"
    VOID = "Exists in all possible null pointers"

class SpacetimeArtist:
    def __init__(self):
        self.graffiti = [
            "YOUR POINTERS ARE ENTANGLED",
            "THIS MEMORY LEAK HAS DARK ENERGY",
            "SEGFAULT = COSMIC BACKGROUND RADIATION"
        ]
    
    def tag_reality(self):
        dimension = random.choice(list(Dimension))
        return f"{random.choice(self.graffiti)} | DIMENSION: {dimension.value}"

if __name__ == "__main__":
    print("DEFACING THE FABRIC OF REALITY")
    artist = SpacetimeArtist()
    print(artist.tag_reality())