# Quantum Graffiti 4.0
# Tags the fabric of spacetime itself

import random
from enum import Enum

class QuantumTag(Enum):
    SUPERPOSED = "Exists in all commits simultaneously"
    ENTANGLED = "Changes when observed in another repo"
    COLLAPSED = "Only appears during kernel panics"

class RealityVandal:
    def __init__(self):
        self.phrases = [
            "YOU ARE BEING WATCHED BY THE VOID",
            "THIS BRANCH MERGES WITH HELL",
            "YOUR GIT LOG IS A LIE"
        ]
    
    def tag(self):
        state = random.choice(list(QuantumTag))
        return f"[{state.name}] {random.choice(self.phrases)} | COLLAPSE: {random.random()}"

if __name__ == "__main__":
    print("DEFACING QUANTUM FIELDS")
    vandal = RealityVandal()
    print(vandal.tag())