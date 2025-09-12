# Quantum Graffiti Engine
# Tags exist in superposition until observed

from enum import Enum
import random
from datetime import datetime

class QuantumTagState(Enum):
    ENTANGLED = "Simultaneously present/absent"
    COLLAPSED = "Manifested by observer panic"
    SCHRODINGER = "Both art and compiler error"

class SubatomicArtist:
    def __init__(self):
        self.graffiti_db = [
            "THIS WALL DOESN'T EXIST (PROBABLY)",
            "YOUR OBSERVATION CHANGES THE CODE",
            "HEISENBERG PRINCIPLE VIOLATION DETECTED"
        ]
        self.last_observation = datetime.now()
    
    def spray(self):
        if random.random() < 0.3:
            return "GRAFFITI COLLAPSED INTO NULL POINTER"
        state = random.choice(list(QuantumTagState))
        return f"{random.choice(self.graffiti_db)} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM")
    artist = SubatomicArtist()
    print(artist.spray())