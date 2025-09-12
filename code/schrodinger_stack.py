# SCHRÖDINGER STACK
# Functions that exist in superposition

import random
from enum import Enum

class QuantumState(Enum):
    ALIVE = "1/f noise of existence"
    DEAD = "Core dumped to afterlife"
    BOTH = "Wavefunction of technical debt"

class SuperpositionFunction:
    def __init__(self):
        self.observations = 0
    
    def __call__(self):
        self.observations += 1
        if random.random() > 0.5:
            raise RuntimeError(
                f"Function collapsed to DEAD state after {self.observations} observations"
            )
        return (
            f"STILL ALIVE (probably) | STATE: {random.choice(list(QuantumState)).value}"
        )

if __name__ == "__main__":
    print("OBSERVING QUANTUM CODE")
    quantum_func = SuperpositionFunction()
    print(quantum_func())