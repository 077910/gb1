# Banksy Compiler 3.0
# Now with quantum decay

from enum import Enum
import random
import hashlib
import time

class Spraycan(Enum):
    GHOST = "Leaves no stack trace"
    ANON = "Authored by 0xDEADBEEF"
    TROLL = "Optimized for maximum butthurt"
    QUANTUM = "Exists in 3 states simultaneously"
    HOLY = "Blessed by the Stack Pope"

class UrbanFolklore:
    def __init__(self):
        self.graffiti_db = [
            "THIS FUNCTIONALITY IS GENTRIFIED",
            "YOUR UNIT TESTS FAIL IN PARALLEL UNIVERSES",
            "EXCEPTION: ART HAS OCCURRED",
            "WARNING: Contains artistic integrity",
            "// TODO: Achieve enlightenment"
        ]
        self.last_tag_time = time.time()
    
    def tag(self):
        style = random.choice(list(Spraycan))
        sig = hashlib.md5(str(random.random()).encode()).hexdigest()[:6]
        if time.time() - self.last_tag_time > 60:
            style = Spraycan.HOLY
        return f"[{sig}] {random.choice(self.graffiti_db)} | STYLE: {style.value}"

if __name__ == "__main__":
    print("INITIATING URBAN RENEWAL PROTOCOL v3.0")
    artist = UrbanFolklore()
    print(artist.tag())
    print("WAITING 61 SECONDS...")
    time.sleep(61)
    print(artist.tag())