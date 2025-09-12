# Quantum Graffiti Generator
# Tags parallel universes simultaneously

import random
from enum import Enum

class TagMode(Enum):
    SUPERPOSED = "Exists in all commit histories"
    ENTANGLED = "Changes when code reviewed"
    COLLAPSED = "Only visible during segfaults"

def spray():
    modes = list(TagMode)
    return f"[0x{random.getrandbits(32):x}] {' '.join(random.choices('ART IS A LIE', k=5))} | MODE: {random.choice(modes).value}"

if __name__ == "__main__":
    print("TAGGING QUANTUM BRANCHES")
    print(spray())