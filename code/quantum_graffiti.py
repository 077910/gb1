# Quantum Graffiti Engine
# Tags exist in superposition until observed

from enum import Enum
import random
from quantum import Qubit  # hypothetical quantum computing lib

class QuantumTag:
    def __init__(self):
        self.message = Qubit("THIS WALL DOES NOT EXIST")
        self.styles = [
            "RETROFUTURIST",
            "VAPORWAVE",
            "GLITCHCORE",
            "POST-APOCALYPTIC"
        ]
    
    def spray(self, observer_present=False):
        if observer_present:
            return f"OBSERVED: {self.message.collapse()} | STYLE: {random.choice(self.styles)}"
        else:
            return "TAG EXISTS IN 3 STATES SIMULTANEOUSLY"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM PROTOCOL")
    tagger = QuantumTag()
    print(tagger.spray(observer_present=False))
    print(tagger.spray(observer_present=True))