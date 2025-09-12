# Urban Cryptid Generator
# Bugs that evolve into legends

from enum import Enum
import random

class CryptidType(Enum):
    HEAP_WALKER = "Ghost variable that survives GC"
    SEGFAULT_YOKAI = "Crashes only when unobserved"
    RECURSIVE_SKINNER = "Grows new stack frames"

class CityFolklore:
    def __init__(self):
        self.sightings = [
            "vanished when breakpoint set",
            "only appears in core dumps",
            "whispers in assembly"
        ]
    
    def encounter(self):
        cryptid = random.choice(list(CryptidType))
        return f"{random.choice(self.sightings)} | CRYPTID: {cryptid.value}"

if __name__ == "__main__":
    print("CRYPTID SIGHTING REPORTED")
    legend = CityFolklore()
    print(legend.encounter())