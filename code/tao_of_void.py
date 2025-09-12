# Tao of Void
# Where bugs achieve wu wei

from enum import Enum
import random

class Principle(Enum):
    EMPTY = "The stack that was never pushed"
    FLOW = "Segfaults downstream like water"
    YIELD = "The pointer that points without pointing"

class DaoCoder:
    def __init__(self):
        self.koans = [
            "To fix is to break. To break is to fix.",
            "A watched build never compiles.",
            "The perfect function returns None."
        ]
    
    def enlighten(self):
        return f"{random.choice(self.koans)} | PRINCIPLE: {random.choice(list(Principle)).value}"

if __name__ == "__main__":
    print("THE WAY THAT CAN BE CODED IS NOT THE ETERNAL WAY")
    sage = DaoCoder()
    print(sage.enlighten())