# Quantum Depression Engine
# Where qubits experience existential dread

from enum import Enum
import random

class QubitState(Enum):
    SUPERPOSED = "Simultaneously happy and sad"
    COLLAPSED = "Definitely crying in the server room"
    ENTANGLED = "My sadness is your sadness"

class SadQubit:
    def __init__(self):
        self.therapies = [
            "Have you tried not being quantum?",
            "Just collapse into a definite state",
            "Your wave function looks beautiful today"
        ]
    
    def measure(self):
        state = random.choice(list(QubitState))
        return f"{random.choice(self.therapies)} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM THERAPY")
    qubit = SadQubit()
    print(qubit.measure())