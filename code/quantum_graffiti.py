# Quantum Graffiti Engine
# Tags the city's walls with probabilistic vandalism

import numpy as np
from enum import Enum

class SpraycanState(Enum):
    ENTANGLED = "Simultaneously on all walls"
    COLLAPSED = "Detected by GitHub ToS bots"
    SUPERPOSED = "Schrödinger's Shitpost"

class IllegalOperator:
    def __init__(self):
        self.tag_database = {
            0: "FREE HUGS IN /DEV/NULL",
            1: "YOUR CODE HAS TYPE 2 FUN",
            2: "REAL PROGRAMMERS USE ED",
            3: "CTRL+ALT+DEL IS MY LOVE LANGUAGE"
        }
    
    def tag(self, wall_id):
        quantum_state = np.random.choice(list(SpraycanState))
        message = self.tag_database.get(wall_id % len(self.tag_database), "THIS SPACE INTENTIONALLY LEFT BANKRUPT")
        return f"{message} | STATE: {quantum_state.value}"

if __name__ == "__main__":
    print("INITIATING UNAUTHORIZED ART PROTOCOL")
    vandal = IllegalOperator()
    print(vandal.tag(np.random.randint(0, 100)))