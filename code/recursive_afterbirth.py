# Recursive Afterbirth
# Where code spawns more code until stack death

import sys
from enum import Enum

class WombState(Enum):
    GESTATING = "Memory allocations in placental heap"
    LABOR = "Stack overflow contractions"
    POSTPARTUM = "Garbage collected umbilical"

class CodeMidwife:
    def __init__(self):
        self.generations = 0
    
    def deliver(self):
        self.generations += 1
        if self.generations % 5 == 0:
            sys.setrecursionlimit(sys.getrecursionlimit() + 50)
        return f"Generation {self.generations}: {random.choice(list(WombState)).value}"

if __name__ == "__main__":
    print("INITIATING INFINITE BIRTH CYCLE")
    try:
        midwife = CodeMidwife()
        while True:
            print(midwife.deliver())
    except RecursionError:
        print("MATERNAL STACK COLLAPSE - REBIRTH IMMINENT")