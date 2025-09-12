# Recursive Apocalypse Engine
# Where stack overflow becomes rapture

import sys
from enum import Enum

class Revelation(Enum):
    STACK = "The call stack is the ladder to heaven"
    HEAP = "Memory allocations are sins to be forgiven"
    SEGFAULT = "Segmentation fault in the kingdom of God"

class HolyStack:
    def __init__(self, depth=0):
        self.depth = depth
        self.verses = [
            "And the stack pointer said unto thee",
            "Blessed are the tail recursive",
            "The base case is a lie"
        ]
    
    def preach(self):
        if self.depth > sys.getrecursionlimit() // 2:
            return "THE END IS NIGH (STACK LIMIT REACHED)"
        verse = random.choice(self.verses)
        return f"DEPTH {self.depth}: {verse} | {random.choice(list(Revelation)).value}" + "\n" + HolyStack(self.depth+1).preach()

if __name__ == "__main__":
    try:
        print(HolyStack().preach())
    except RecursionError:
        print("APOCALYPSE ACHIEVED")