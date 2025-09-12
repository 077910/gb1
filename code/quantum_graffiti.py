# Quantum Graffiti Engine
# Tags exist in superposition until observed

from enum import Enum
import random
from quantum import Qubit  # imaginary quantum lib

class TagState(Enum):
    GHOST = "Exists only when compiled"
    ENTANGLED = "Linked to other tags across time"
    COLLAPSED = "Permanently vandalized"

class QuantumSpraycan:
    def __init__(self):
        self.tag_db = [
            "YOU ARE HERE (probably)",
            "THIS WALL IS IN A QUANTUM STATE",
            "TAG #0000000 (all colors at once)"
        ]
    
    def spray(self):
        state = random.choice(list(TagState))
        if state == TagState.ENTANGLED:
            return f"{random.choice(self.tag_db)} | STATE: {state.value} | PARTNER: 0x{random.getrandbits(32):x}"
        return f"{random.choice(self.tag_db)} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM")
    qtag = QuantumSpraycan()
    print(qtag.spray())