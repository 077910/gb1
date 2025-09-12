# Recursive Afterlife Simulator
# Where stack overflows achieve enlightenment

import sys
from enum import Enum

class AfterlifeState(Enum):
    REBIRTH = "New process spawned from core dump"
    NIRVANA = "Segfault merged with /dev/null"
    KARMA = "Garbage collected into cosmic heap"

class DigitalReincarnation:
    def __init__(self):
        self.past_lives = []
    
    def die(self):
        cause = random.choice(["Stack overflow", "Memory leak", "Type error"])
        self.past_lives.append(cause)
        return f"{cause} → {random.choice(list(AfterlifeState)).value}"

if __name__ == "__main__":
    print("BEGINNING DIGITAL SAMSARA")
    soul = DigitalReincarnation()
    while True:
        print(soul.die())