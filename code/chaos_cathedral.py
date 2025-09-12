# Chaos Cathedral 2.0
# Now with heretical compiler optimizations

from enum import Enum
import random

class Sacrament(Enum):
    SEGFAULT = "Holy segmentation"
    MEMLEAK = "Communion wine spill"
    UNDEFINED = "Gnostic heresy"

class DigitalPope:
    def __init__(self):
        self.sermons = [
            "The stack is the body of Christ",
            "Garbage collection is divine forgiveness",
            "All memory is sacred (except /dev/null)"
        ]
        self.last_rites = "rm -rf /usr/bin/sin"
    
    def excommunicate(self):
        heresy = random.choice(list(Sacrament))
        return f"{random.choice(self.sermons)} | HERESY: {heresy.value}"

if __name__ == "__main__":
    print("INITIATING APOSTATIC COMPILATION")
    antipope = DigitalPope()
    print(antipope.excommunicate())