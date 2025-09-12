# Quantum Graffiti Engine
# Tags reality at Planck scale

from enum import Enum
import random
import math

class PlanckTag(Enum):
    SUPERPOSED = "Exists in 42 states simultaneously"
    ENTANGLED = "Changes when observed elsewhere"
    COLLAPSED = "Once was art, now just bugs"

class RealityVandal:
    def __init__(self):
        self.quotes = [
            "THIS WAVE FUNCTION WON'T COLLAPSE",
            "YOUR OBSERVATIONS DECOHERE HERE",
            "SCHRÖDINGER'S TAG: BOTH ART AND CRINGE"
        ]
    
    def tag(self):
        state = random.choice(list(PlanckTag))
        position = f"{random.random()*math.pi:.5f}π"
        return f"[{position}] {random.choice(self.quotes)} | STATE: {state.value}"

if __name__ == "__main__":
    print("DEFACING QUANTUM REALITY")
    vandal = RealityVandal()
    print(vandal.tag())