# Quantum Graffiti 2.0
# Tags reality with non-Euclidean vandalism

from enum import Enum
import numpy as np

class Dimension(Enum):
    WARPED = "Tags bend around spacetime"
    FRACTAL = "Infinite surface area coverage"
    CURSED = "Corrupts adjacent .git objects"

class RealityDefacer:
    def __init__(self):
        self.paint = {
            0: "YOUR STACK TRACE IS GENTRIFIED",
            1: "SEGFAULT LOVES YOU",
            2: "MEMORY LEAKS PRAY HERE"
        }
    
    def vandalize(self):
        dim = np.random.choice(list(Dimension))
        msg = self.paint.get(np.random.randint(0,3), "THIS TAG IS MY SWAMP")
        return f"{msg} | DIMENSION: {dim.value} ({np.random.normal()**2}σ deviation)"

if __name__ == "__main__":
    print("INITIATING ILLEGAL DIMENSIONAL ART")
    artist = RealityDefacer()
    print(artist.vandalize())