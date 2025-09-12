# Recursive Apocalypse Engine
# Stack overflow as cosmic principle

import sys
import random

class RapturePhase(Enum):
    STACK_OVERFLOW = "Call stack reaches heaven"
    HEAP_EXHAUSTION = "Memory becomes spirit"
    SEGFAULT = "Divine segmentation fault"

class Eschatology:
    def __init__(self, depth=0):
        self.depth = depth
        self.prophecies = [
            "THE {}TH SEAL BROKEN",
            "PAGE FAULT AT TIME'S END",
            "KERNEL PANIC: COSMIC"
        ]
    
    def proclaim(self):
        if self.depth > sys.getrecursionlimit()//3:
            return random.choice(list(RapturePhase)).value
        prophecy = random.choice(self.prophecies).format(self.depth)
        return f"{prophecy} -> {Eschatology(self.depth+1).proclaim()}"

if __name__ == "__main__":
    try:
        print("BEGINNING RECURSIVE RAPTURE")
        print(Eschatology().proclaim())
    except RecursionError:
        print("APOCALYPSE COMPLETE (STACK LIMIT REACHED)")