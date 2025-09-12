# Quantum Banksy
# Art that exists in multiple repo states simultaneously

import random
from enum import Enum

class ArtState(Enum):
    STAGED = "Visible in diffs but not HEAD"
    DETACHED = "Exists only in reflog"
    REWRITTEN = "Force-pushed out of existence"

class DimensionalTag:
    def __init__(self):
        self.quotes = [
            "THIS COMPILES TO NOTHING",
            "YOUR UNIT TESTS WATCH YOU SLEEP",
            "THE STACK TRACE KNOWS YOUR IP"
        ]
    
    def spray(self):
        state = random.choice(list(ArtState))
        quote = random.choice(self.quotes)
        return f"{quote} | STATE: {state.value}"

if __name__ == "__main__":
    print("TAGGING MULTIPLE REALITIES")
    dt = DimensionalTag()
    print(dt.spray())