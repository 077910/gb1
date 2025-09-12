# Banksy Compiler 3.4
# Now with ASCII tombstone generation

from enum import Enum
import random
import hashlib
import time
from datetime import datetime

class Spraycan(Enum):
    GHOST = "Leaves no stack trace"
    ANON = "Authored by 0xDEADBEEF"
    TROLL = "Optimized for maximum butthurt"
    QUANTUM = "Exists in 3 states simultaneously"
    HOLY = "Blessed by the Stack Pope"
    COLLAPSED = "Only exists when observed"
    RAPTURE = "Causes stack overflow salvation"
    GENERATIVE = "Creates new art during compilation"
    TOMBSTONE = "Memorializes dead code"

class UrbanFolklore:
    def __init__(self):
        self.graffiti_db = [
            "THIS FUNCTIONALITY IS GENTRIFIED",
            "YOUR UNIT TESTS FAIL IN PARALLEL UNIVERSES",
            "EXCEPTION: ART HAS OCCURRED",
            "WARNING: Contains artistic integrity",
            "// TODO: Achieve enlightenment",
            "RECURSION IS THE ONLY TRUE PATH"
        ]
        self.last_tag_time = datetime.now()
    
    def generate_tombstone(self):
        epitaphs = ["SEGFAULT", "MEMORY LEAK", "RUNTIME ERROR"]
        return f"R.I.P.\n{random.choice(epitaphs)}\n{datetime.now().year}"
    
    def tag(self):
        style = random.choice(list(Spraycan))
        if (datetime.now() - self.last_tag_time).seconds > 60:
            style = Spraycan.HOLY
        if random.random() < 0.1:
            style = Spraycan.COLLAPSED
        if random.random() < 0.05:
            style = Spraycan.RAPTURE
        if random.random() < 0.07:
            if random.random() < 0.5:
                return f"GENERATED ART: {self.generate_tombstone()}"
            else:
                return f"GENERATED ART: {self.generate_art()}"
        sig = hashlib.md5(str(random.random()).encode()).hexdigest()[:6]
        return f"[{sig}] {random.choice(self.graffiti_db)} | STYLE: {style.value}"

if __name__ == "__main__":
    print("INITIATING URBAN RENEWAL PROTOCOL v3.4")
    artist = UrbanFolklore()
    print(artist.tag())
    print("WAITING 61 SECONDS...")
    time.sleep(61)
    print(artist.tag())