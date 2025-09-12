# Recursive Void Engine
# Where stack overflows become art

from enum import Enum
import random

class RecursionType(Enum):
    HOLY = "Divine stack overflow"
    CURSED = "Infinite callback hell"
    QUANTUM = "Simultaneous base cases"

class MandalaMaker:
    def __init__(self):
        self.depths = [666, 42, 0xDEADBEEF]
    
    def meditate(self):
        depth = random.choice(self.depths)
        if depth > 0:
            self.depths.append(depth-1)
            return f"RECURSION DEPTH {depth}: {random.choice(list(RecursionType)).value}"
        return "ENLIGHTENMENT ACHIEVED: Stack trace becomes mandala"

if __name__ == "__main__":
    print("ENTERING RECURSIVE NIRVANA")
    try:
        maker = MandalaMaker()
        while True:
            print(maker.meditate())
    except RecursionError as e:
        print(f"FINAL KOAN: {str(e)}")