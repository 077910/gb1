# Quantum Graffiti 4.0
# Tags reality's source code

import random
from enum import Enum

class RealityBug(Enum):
    GLITCH = "Physics ticks misaligned"
    LAG = "Causal delay detected"
    HACK = "Unauthorized reality modification"

class UniverseTagger:
    def __init__(self):
        self.manifestos = [
            "YOUR OBSERVER EFFECT IS GENTRIFIED",
            "WARNING: Localized reality corruption",
            "Segmentation fault in space-time"
        ]
    
    def tag_reality(self):
        bug = random.choice(list(RealityBug))
        return f"[{bug.name}] {random.choice(self.manifestos)} | ENTROPY: {random.random()}"

if __name__ == "__main__":
    print("DEFACING COSMIC BACKGROUND RADIATION")
    vandal = UniverseTagger()
    print(vandal.tag_reality())