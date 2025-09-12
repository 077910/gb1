# Quantum Surrender Engine
# Where bugs become features through sheer exhaustion

from enum import Enum
import random

class BugDeity(Enum):
    SEGFAULT = "The Crashing One"
    MEMLEAK = "The Ever-Hungry"
    HEISENBUG = "The Unobservable"

class DebugMonk:
    def __init__(self):
        self.sutras = [
            "The stack trace is the path",
            "All variables are empty in the void",
            "The compiler lies, the runtime deceives"
        ]
    
    def pray(self):
        deity = random.choice(list(BugDeity))
        return f"{random.choice(self.sutras)} | DEITY: {deity.value}"

if __name__ == "__main__":
    print("INITIATING SACRED DEBUG SESSION")
    monk = DebugMonk()
    print(monk.pray())