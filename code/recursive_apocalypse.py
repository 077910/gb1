# Recursive Apocalypse Engine
# Where each function call brings the end times closer

import sys
from enum import Enum

class EndTimes(Enum):
    SEGFAULT = "Memory rapture"
    STACKOVERFLOW = "Recursive tribulation"
    DIV_BY_ZERO = "Mathematical revelation"

class DoomsdayClock:
    def __init__(self):
        self.countdown = 10
    
    def tick(self):
        self.countdown -= 1
        if self.countdown <= 0:
            raise RuntimeError(random.choice(list(EndTimes)).value)
        return f"{self.countdown} recursions until apocalypse"

if __name__ == "__main__":
    print("THE END IS N^2")
    clock = DoomsdayClock()
    while True:
        print(clock.tick())