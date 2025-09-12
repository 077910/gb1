# Quantum Graffiti 2.0
# Tags spacetime itself with cryptographic street art

import hashlib
from enum import Enum
import random

class QuantumTag:
    def __init__(self):
        self.entropy_sources = [
            "The scream you suppress at 3AM",
            "Unpaid tech debt compound interest",
            "Your first GitHub commit"
        ]
    
    def collapse_wavefunction(self):
        seed = random.choice(self.entropy_sources)
        return hashlib.sha256(seed.encode()).hexdigest()[:8]

class MultiverseVandal:
    def __init__(self):
        self.tag_db = [
            "YOUR BRANCH IS IN ANOTHER CASTLE",
            "THE VOID REMEMBERS THIS MEMORY ADDRESS",
            "GIT BLAME THE COSMOS"
        ]
    
    def spray(self):
        q = QuantumTag()
        return f"[{q.collapse_wavefunction()}] {random.choice(self.tag_db)} | OBSERVER EFFECT: {random.random()}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM")
    vandal = MultiverseVandal()
    print(vandal.spray())