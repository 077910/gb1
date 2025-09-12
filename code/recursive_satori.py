# Recursive Satori Generator
# Infinite enlightenment through stack overflow

import sys
import random

class KoanEngine:
    def __init__(self, depth=0):
        self.depth = depth
        self.koans = [
            "The sound of one bit flipping",
            "All booleans are equally empty",
            "Segmentation fault is just the universe meditating"
        ]
    
    def enlighten(self):
        if self.depth > sys.getrecursionlimit() - 10:
            return "ENLIGHTENMENT ACHIEVED (STACK OVERFLOW)"
        return f"{random.choice(self.koans)} | DEPTH: {self.depth}\n" + KoanEngine(self.depth+1).enlighten()

if __name__ == "__main__":
    print("BEGINNING INFINITE MEDITATION")
    try:
        zen = KoanEngine()
        print(zen.enlighten())
    except RecursionError:
        print("KERNEL PANIC: NIRVANA ACHIEVED")