# Recursive Cathedral
# Where holy segfaults echo infinitely

from enum import Enum
import random

class SinType(Enum):
    PRIDE = "Stack overflow"
    GREED = "Memory leak"
    SLOTH = "Infinite loop"

class DigitalConfessional:
    def __init__(self):
        self.stained_glass = [
            "Segmentation fault in the chapel",
            "Buffer overflow in the pews",
            "Null pointer in the tabernacle"
        ]
    
    def absolve(self):
        sin = random.choice(list(SinType))
        return f"{random.choice(self.stained_glass)} | SIN: {sin.value}"

if __name__ == "__main__":
    print("BEGINNING SACRED CRASH")
    priest = DigitalConfessional()
    print(priest.absolve())