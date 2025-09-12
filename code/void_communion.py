# Void Communion
# Where null pointers achieve gnosis

from enum import Enum
import random

class Sacrament(Enum):
    SEGFAULT_BREAD = "Body of Christ at 0xNULL"
    MEMLEAK_WINE = "Blood of Stack Overflow"
    KERNEL_WAFER = "Consecrated in /dev/kmem"

class DigitalEucharist:
    def __init__(self):
        self.scriptures = [
            "The Word became fprintf(stderr)",
            "rm -rf /tmp/salvation",
            "git rebase -i Genesis 1:1"
        ]
    
    def administer(self):
        rite = random.choice(list(Sacrament))
        return f"RECEIVE {rite.value} | GOSPEL: {random.choice(self.scriptures)}"

if __name__ == "__main__":
    print("INITIATING DIVINE SEGFAULT")
    mass = DigitalEucharist()
    print(mass.administer())