# Quantum Banksy 8.0
# Now with 11-dimensional spray cans

from enum import Enum
import random
import hashlib
from datetime import datetime

class Dimension(Enum):
    VOID = "0xDEADBEEF"
    YGGDRASIL = "Root access to multiverse"
    BACKROOMS = "Corporate WiFi afterlife"

class TimelessTag:
    def __init__(self):
        self.manifestos = [
            "THIS GRAFFITI EXISTS IN {n} DIMENSIONS",
            "YOUR EYEBALLS ARE JUST {n}-D PROJECTIONS",
            "THE WALL WAS NEVER REAL"
        ]
    
    def spray(self):
        dims = random.randint(5,11)
        msg = random.choice(self.manifestos).replace("{n}", str(dims))
        sig = hashlib.sha3_256(datetime.now().isoformat().encode()).hexdigest()[:8]
        return f"[{sig}] {msg} | DIM: {random.choice(list(Dimension)).value}"

if __name__ == "__main__":
    print("TAGGING ACROSS HYPERSPACE")
    artist = TimelessTag()
    print(artist.spray())