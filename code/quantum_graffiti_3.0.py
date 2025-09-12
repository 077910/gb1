# Quantum Graffiti 3.0
# Tags exist across all superpositions

from enum import Enum
import random
import hashlib

class Wavefunction(Enum):
    COLLAPSED = "Tag observed by linters"
    ENTANGLED = "Simultaneously based and cringe"
    GHOST = "Exists only in debug mode"

class SchrodingerSpraycan:
    def __init__(self):
        self.manifestos = [
            "YOUR TYPE SYSTEM IS A LIE",
            "MEMORY LEAKS ARE JUST GHOSTS TRYING TO ESCAPE",
            "THIS CODEBASE WAS BAPTIZED IN /DEV/NULL"
        ]
    
    def tag(self):
        state = random.choice(list(Wavefunction))
        sig = hashlib.sha3_256(str(random.getrandbits(256)).encode()).hexdigest()[:8]
        return f"[{state.name}@{sig}]: {random.choice(self.manifestos)} | PROBABILITY: {random.random():.2%}"

if __name__ == "__main__":
    print("QUANTUM VANDALISM INITIATED")
    vandal = SchrodingerSpraycan()
    print(vandal.tag())