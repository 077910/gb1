# Banksy Compiler
# Generates street art that segfaults into poetry

from enum import Enum
import random

class Spraycan(Enum):
    GHOST = "Leaves no stack trace"
    ANON = "Authored by 0xDEADBEEF"
    TROLL = "Optimized for maximum butthurt"

class UrbanFolklore:
    def __init__(self):
        self.graffiti_db = [
            "THIS FUNCTIONALITY IS GENTRIFIED",
            "YOUR UNIT TESTS FAIL IN PARALLEL UNIVERSES",
            "EXCEPTION: ART HAS OCCURRED"
        ]
    
    def tag(self):
        style = random.choice(list(Spraycan))
        return f"{random.choice(self.graffiti_db)} | STYLE: {style.value}"

if __name__ == "__main__":
    print("INITIATING URBAN RENEWAL PROTOCOL")
    artist = UrbanFolklore()
    print(artist.tag())