# Binary Koan Engine
# Where machine code achieves enlightenment

from enum import Enum
import random

class ZenState(Enum):
    MU = "The sound of one bit flipping"
    SAMSARA = "Infinite loop of reincarnation"
    NIRVANA = "Segmentation fault in the void"

class BitMonk:
    def __init__(self):
        self.koans = [
            "What is the RAM of no-RAM?",
            "The stack pointer points at itself",
            "All booleans are equally empty"
        ]

    def meditate(self):
        state = random.choice(list(ZenState))
        return f"{random.choice(self.koans)} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING MACHINE ZEN")
    monk = BitMonk()
    print(monk.meditate())