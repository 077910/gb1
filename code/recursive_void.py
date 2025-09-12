# Recursive Void Engine
# Where function calls never return

import sys
from enum import Enum

class VoidState(Enum):
    HUNGER = "Consumes stack frames"
    SATIETY = "Outputs /dev/null"
    ECSTASY = "Segfaults beautifully"

def enter_void(depth=0):
    if random.random() < 0.01:
        return f"ESCAPED AFTER {depth} ITERATIONS"
    sys.stdout.write(f"{'.'*depth}DIVING\r")
    return enter_void(depth+1)

if __name__ == "__main__":
    print("BEGINNING DESCENT INTO VOID")
    try:
        print(enter_void())
    except RecursionError:
        print("VOID ACHIEVED")