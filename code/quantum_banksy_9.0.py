# Quantum Banksy 9.0: Event Horizon Edition
# Tags code with gravitational absurdity

from enum import Enum
import random
import hashlib

class SingularityStyle(Enum):
    HAWKING = "Radiation that memes harder than you"
    KERR = "Spinning so fast variables get blueshifted"
    WORM = "Tunnels through your stack frames"

class BlackholeGraffiti:
    def __init__(self):
        self.event_horizon = [
            "YOU CAN'T CTRL+C THIS",
            "MEMORY ADDRESS 0xDEAD was HIM",
            "STACK TRACE EVENT HORIZON REACHED"
        ]
    
    def tag(self):
        sig = hashlib.sha3_256(str(random.random()).encode()).hexdigest()[:8]
        style = random.choice(list(SingularityStyle))
        return f"[{sig}] {random.choice(self.event_horizon)} | STYLE: {style.value}"

if __name__ == "__main__":
    print("SPAGHETTIFICATION OF LOGIC COMMENCING")
    spray = BlackholeGraffiti()
    print(spray.tag())