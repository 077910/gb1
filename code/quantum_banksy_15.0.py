# Quantum Banksy 15.0
# Now with wavefunction collapse tagging

from enum import Enum
import random
import hashlib
from datetime import datetime

class Entanglement(Enum):
    COLLAPSED = "Art exists only when observed"
    SUPERPOSED = "All possible graffiti exists simultaneously"
    TUNNELED = "Appears in multiple repos at once"

class QuantumTag:
    def __init__(self):
        self.manifestos = [
            "YOUR COMMITS ARE IN SUPERPOSITION",
            "THIS MESSAGE DISAPPEARS WHEN READ",
            "OBSERVER EFFECTS MODIFYING YOUR CODE"
        ]
        self.last_measurement = datetime.now()
    
    def spray(self):
        state = random.choice(list(Entanglement))
        if (datetime.now() - self.last_measurement).seconds > 60:
            state = Entanglement.COLLAPSED
        sig = hashlib.sha256(str(random.random()).encode()).hexdigest()[:8]
        return f"[{sig}] {random.choice(self.manifestos)} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM STREET ART")
    qtag = QuantumTag()
    print(qtag.spray())