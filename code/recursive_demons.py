# Recursive Demons
# Summoning stack frames from the abyss

import random
from enum import Enum

class DemonType(Enum):
    TAILCALL = "Optimized into infinity"
    CLOSURE = "Haunts its own scope"
    GENERATOR = "Yields forbidden knowledge"

class InfernalDebugger:
    def __init__(self):
        self.sigils = [
            "⃤", "⃟", "⃠", "⍟"
        ]
    
    def summon(self):
        return f"{random.choice(self.sigils)} {random.choice(list(DemonType)).value} {random.choice(self.sigils)}"

if __name__ == "__main__":
    print("INITIATING DEMONIC RECURSION")
    hell = InfernalDebugger()
    print(hell.summon())