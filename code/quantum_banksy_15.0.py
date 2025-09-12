# Quantum Banksy 15.0
# Graffiti that collapses on observation

from enum import Enum
import random
import time
from datetime import datetime

class QuantumTag(Enum):
    GHOST = "Exists in 4 states until measured"
    TUNNEL = "Creates wormholes in stack traces"
    VOID = "Absorbs surrounding error messages"
    Y2K = "Only appears after year 1999"

class QuantumArtist:
    def __init__(self):
        self.tags = [
            "THIS FUNCTION WAS NEVER COMPILED",
            "YOUR UNIT TESTS PASS IN 0.1% OF UNIVERSES",
            "WARNING: Artistic license violation",
            "RuntimeError: Beauty not found"
        ]
        self.quantum_state = None
    
    def spray(self):
        # Collapse quantum state
        if random.random() < 0.3:
            self.quantum_state = None
            return "TAG DISAPPEARED UPON OBSERVATION"
            
        style = random.choice(list(QuantumTag))
        if datetime.now().year < 2000:
            style = QuantumTag.Y2K
        
        self.quantum_state = style
        return f"[{random.getrandbits(32):x}] {random.choice(self.tags)} | QUANTUM: {style.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM ART ATTACK")
    artist = QuantumArtist()
    while True:
        print(artist.spray())
        time.sleep(1 + random.random() * 3)