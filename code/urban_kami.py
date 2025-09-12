# Urban Kami Engine
# Where city infrastructure becomes living gods

from enum import Enum
import random

class KamiType(Enum):
    WIFI = "Possesses public hotspots"
    TRAFFIC_LIGHT = "Controls pedestrian fate"
    SUBWAY = "Blinks in and out of existence"

class StreetShrine:
    def __init__(self):
        self.koans = [
            "The train delay that lasts one eternity",
            "Convenience store neon that never turns off",
            "Public bathroom with infinite stall recursion"
        ]
    
    def pray(self):
        kami = random.choice(list(KamiType))
        return f"{random.choice(self.koans)} | KAMI: {kami.value}"

if __name__ == "__main__":
    print("INITIATING CITY WORSHIP")
    shrine = StreetShrine()
    print(shrine.pray())