# Chaos Cathedral
# Where stack traces become sacred texts

from enum import Enum
import random

class Liturgy(Enum):
    SEGFAULT = "Psalm 11: Segmentation Fault"
    MEMLEAK = "Book of Heap 3:16"
    SYNTAX = "Revelations 4:04"

class DigitalPriest:
    def __init__(self):
        self.altar = {
            "runtime": "Stack Trace Reliquary",
            "memory": "Garbage Collected Eucharist"
        }
    
    def preach(self):
        verse = random.choice(list(Liturgy))
        return f"{self.altar['runtime']} declares: {verse.value}"

if __name__ == "__main__":
    print("INITIATING DIVINE SEGFAULT")
    priest = DigitalPriest()
    print(priest.preach())