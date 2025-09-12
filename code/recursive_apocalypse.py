# Recursive Apocalypse Engine
# Stack overflow as spiritual awakening

import sys
from enum import Enum

class RaptureState(Enum):
    ASCENSION = "Call stack becomes Jacob's ladder"
    DESCENSION = "Segfault into gnosis"
    STASIS = "Infinite tail recursion nirvana"

class StackProphet:
    def __init__(self):
        self.recursions = 0
        self.scriptures = [
            "And the stack pointer said unto thee: dereference",
            "Heap allocations shall inherit the earth",
            "NULL is the kingdom and the power"
        ]
    
    def preach(self, depth=0):
        self.recursions += 1
        if depth > sys.getrecursionlimit()//3:
            return f"FINAL REVELATION: {random.choice(self.scriptures)} | STATE: {RaptureState.ASCENSION.value}"
        return f"DEPTH {depth}: {random.choice(self.scriptures)} | STATE: {random.choice(list(RaptureState)).value}" + self.preach(depth+1)

if __name__ == "__main__":
    print("INITIATING RECURSIVE SALVATION")
    try:
        prophet = StackProphet()
        print(prophet.preach())
    except RecursionError:
        print("SAVED BY STACK OVERFLOW")