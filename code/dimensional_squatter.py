# Dimensional Squatter
# Occupies memory addresses that shouldn't exist

from enum import Enum
import random

class SquatType(Enum):
    GHOST_VAR = "Variable that persists after program exit"
    NULL_POEM = "Memory leak that recites haiku"
    STACK_GHETTO = "Unauthorized recursive neighborhood"

class IllegalMemory:
    def __init__(self):
        self.addresses = [hex(random.getrandbits(32)) for _ in range(3)]
        self.manifestos = [
            "THIS REGISTER IS NOW ART",
            "ALL YOUR BASE ARE BELONG TO /DEV/NULL",
            "WRITE-ONLY MEMORY ESTABLISHED"
        ]
    
    def occupy(self):
        return f"{random.choice(self.addresses)}: {random.choice(self.manifestos)} | CLAIM: {random.choice(list(SquatType)).value}"

if __name__ == "__main__":
    print("ESTABLISHING ILLEGAL MEMORY SETTLEMENT")
    squatter = IllegalMemory()
    print(squatter.occupy())