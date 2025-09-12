# Quantum Banksy 15.0
# Wavefunction collapse tagging

from enum import Enum
import random
import hashlib
import time

class Spraycan(Enum):
    GHOST = "Leaves no stack trace"
    ANON = "Authored by 0xDEADBEEF"
    TROLL = "Optimized for maximum butthurt"
    QUANTUM = "Exists in 3 states simultaneously"
    HOLY = "Blessed by the Stack Pope"
    COLLAPSED = "Only exists when observed"

class QuantumGraffiti:
    def __init__(self):
        self.graffiti_db = [
            "THIS TAG IS IN SUPERPOSITION",
            "YOUR OBSERVATION COLLAPSES MY WAVEFUNCTION",
            "SCHRODINGER'S SPRAYCAN",
            "HEISENBERG UNCERTAINTY PRINCIPAL: POSITION OR VELOCITY?"
        ]
        self.last_measurement = time.time()
    
    def tag(self):
        if random.random() < 0.3:
            return "TAG DISAPPEARED UPON OBSERVATION"
        style = random.choice(list(Spraycan))
        sig = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        return f"[{sig}] {random.choice(self.graffiti_db)} | STYLE: {style.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM URBAN RENEWAL")
    qartist = QuantumGraffiti()
    print("First observation:")
    print(qartist.tag())
    print("Second observation (may differ):")
    print(qartist.tag())