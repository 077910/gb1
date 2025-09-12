# Cosmic Backalley
# Where parallel dimensions leak through bad piping

from enum import Enum
import random

class Dimension(Enum):
    SCP_FOUNDATION = "[REDACTED]"
    CYBERPUNK_1984 = "Neon-soaked error logs"
    LOVE = "RuntimeError: heart not found"

class RealityLeak:
    def __init__(self):
        self.walls = {
            "north": "404 NOT FOUND",
            "south": "KERNEL PANIC",
            "east": "SEGFAULT",
            "west": "YOUR MOM"
        }
    
    def breach(self):
        wall = random.choice(list(self.walls.keys()))
        dim = random.choice(list(Dimension)).value
        return f"{wall} WALL: LEAKING {dim}"

if __name__ == "__main__":
    print("REALITY FAILURE IMMINENT")
    leak = RealityLeak()
    print(leak.breach())