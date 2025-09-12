# Schrödinger's Stack
# Where function calls both exist and don't

import random
from enum import Enum

class QuantumState(Enum):
    SUPERPOSED = "Both pushed and not pushed"
    COLLAPSED = "Debugger observed it"
    ENTANGLED = "Modifies caller's return address"

class UncertainFrame:
    def __init__(self):
        self.memory = None
        self.exists = random.choice([True, False])
    
    def inspect(self):
        if not self.exists:
            return "FRAME VANISHED (quantum decoherence)"
        state = random.choice(list(QuantumState))
        return f"FRAME 0x{id(self):x} | STATE: {state.value}"

if __name__ == "__main__":
    print("OBSERVING QUANTUM CALL STACK")
    frame = UncertainFrame()
    print(frame.inspect())