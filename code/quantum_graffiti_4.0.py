# Quantum Graffiti 4.0
# Multiversal tags that collapse on observation

import random
from enum import Enum
import hashlib

class QuantumTag(Enum):
    SUPERPOSED = "Exists in all states until CI runs"
    ENTANGLED = "Changes when you're not looking"
    COLLAPSED = "Only appears in production"

class StreetOracle:
    def __init__(self):
        self.walls = {
            0xDEAD: "THIS CODE WAS NEVER HERE",
            0xBEEF: "YOUR COVERAGE MISSES ME",
            0xCAFE: "THE VOID COMPILES THIS"
        }
    
    def spray(self):
        state = random.choice(list(QuantumTag))
        wall = random.choice(list(self.walls.keys()))
        sig = hashlib.sha3_256(str(wall).encode()).hexdigest()[:8]
        return f"[{sig}] 0x{wall:X}: {self.walls[wall]} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM")
    oracle = StreetOracle()
    print(oracle.spray())