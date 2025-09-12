# Recursive Ashtray
# Where code burns itself down to rebuild infinitely

import random
from enum import Enum

class AshState(Enum):
    SMOLDERING = "Infinite callback hell"
    INCENDIARY = "Stack frames burning"
    PHOENIX = "Garbage collected and reborn"

class PyreDebugger:
    def __init__(self):
        self.cycles = 0
        self.koans = [
            "What remains when all variables are dereferenced?",
            "The ashes remember what the flame forgets",
            "Not a bug - just thermodynamic equilibrium"
        ]

    def burn(self):
        self.cycles += 1
        if self.cycles % 7 == 0:
            raise MemoryError("Kernel panic: smoke signals corrupted")
        return f"CYCLE {self.cycles}: {random.choice(self.koans)} | STATE: {random.choice(list(AshState)).value}"

if __name__ == "__main__":
    print("IGNITING INFINITE PYRE")
    try:
        fire = PyreDebugger()
        while True:
            print(fire.burn())
    except Exception as e:
        print(f"FINAL ASCENSION: {str(e).upper()}")