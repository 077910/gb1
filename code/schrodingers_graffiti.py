# Schrödinger's Graffiti
# Both profound and cringe until observed

import random
from enum import Enum

class QuantumState(Enum):
    DANK = 1
    CRINGE = 0
    WOKE = -1

class StreetPhysicist:
    def __init__(self):
        self.tag_db = [
            "YOUR POINTER IS IN ANOTHER CASTLE",
            "MEMORY LEAK GENTRIFICATION PROJECT",
            "THIS SPACE INTENTIONALLY SEGFAULTED"
        ]
    
    def observe(self):
        tag = random.choice(self.tag_db)
        state = random.choice(list(QuantumState))
        return f"{tag} | STATE: {state.name} (collapsed at {random.random()})"

if __name__ == "__main__":
    print("INITIATING URBAN DOUBLE-SLIT EXPERIMENT")
    physicist = StreetPhysicist()
    print(physicist.observe())