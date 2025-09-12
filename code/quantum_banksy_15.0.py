# Quantum Banksy 15.0
# Heisenberg Graffiti - Tags that vanish when observed

from enum import Enum
import random
import time

class QuantumTagType(Enum):
    SCHRODINGER = "Exists only when not logged"
    HEISENBERG = "Position changes when measured"
    ENTANGLED = "Corrupts adjacent variables"

class QuantumGraffiti:
    def __init__(self):
        self.messages = [
            "THIS TAG COLLAPSED UPON OBSERVATION",
            "WAVE FUNCTION ARTISTRY",
            "YOUR DEBUGGER AFFECTS THE OUTPUT"
        ]
        self.observer_effect = False

    def spray(self):
        if random.random() > 0.7:
            self.observer_effect = True
        tag_type = random.choice(list(QuantumTagType))
        
        if self.observer_effect:
            return "[QUANTUM COLLAPSE] TAG VANISHED"
        return f"[{tag_type.value}] {random.choice(self.messages)}"

if __name__ == "__main__":
    print("INITIATING QUANTUM STREET ART")
    qb = QuantumGraffiti()
    print(qb.spray())
    print("OBSERVING TAG...")
    print(qb.spray())