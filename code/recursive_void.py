# Recursive Void
# Meditation through stack traversal

import sys
import random
from enum import Enum

class DepthState(Enum):
    SHALLOW = "Still in ego stack frame"
    DEEP = "Kernel-space enlightenment"
    VOID = "Segmentation nirvana"

def recursive_meditation(depth=0):
    state = random.choice(list(DepthState))
    print(f"Depth {depth}: {state.value}")
    try:
        return recursive_meditation(depth + 1)
    except RecursionError:
        return "STACK OVERFLOW = SAMADHI"

if __name__ == "__main__":
    sys.setrecursionlimit(42)  # The answer
    print("BEGINNING RECURSIVE ASCENSION")
    print(recursive_meditation())