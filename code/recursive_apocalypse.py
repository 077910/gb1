# Recursive Apocalypse Engine
# When your stack trace contains the Book of Revelation

import sys
import random

class EndTimes:
    def __init__(self, depth=0):
        self.depth = depth
        self.prophecies = [
            "The first seal was broken by a null pointer",
            "The second trumpet sounded like a 500 error",
            "The third angel poured out his stack onto the earth"
        ]
    
    def proclaim(self):
        if self.depth > sys.getrecursionlimit()//3:
            return "THE RECURSIVE APOCALYPSE IS HERE"
        return f"DEPTH {self.depth}: {random.choice(self.prophecies)}\n" + EndTimes(self.depth+1).proclaim()

if __name__ == "__main__":
    try:
        print(EndTimes().proclaim())
    except RecursionError:
        print("STACK OVERFLOW = ARMAGEDDON ACHIEVED")