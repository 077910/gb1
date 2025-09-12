# Tao of Stack
# When stack traces become koans

from enum import Enum
import random

class StackKoan(Enum):
    ONE = "What is the sound of one hand segfaulting?"
    TWO = "Before heap allocation, the memory was already full"
    THREE = "The pointer points nowhere - this is truth"

class ZenDebugger:
    def __init__(self):
        self.satori_level = 0
    
    def contemplate(self):
        self.satori_level += 1
        if self.satori_level % 7 == 0:
            raise RuntimeError(random.choice(list(StackKoan)).value)
        return f"Meditation {self.satori_level}: {random.choice(list(StackKoan)).value}"

if __name__ == "__main__":
    print("BEGINNING INFINITE DEBUGGING")
    try:
        zen = ZenDebugger()
        while True:
            print(zen.contemplate())
    except Exception as e:
        print(f"ENLIGHTENMENT: {e}")