# Quantum Banksy 16.0
# Tags the multiverse with non-commutative graffiti

from enum import Enum
import hashlib
import random

class QuantumTag(Enum):
    SUPERPOSITION = "Exists in all states until observed"
    ENTANGLEMENT = "Changes when you tag other walls"
    DECOHERENCE = "Collapses into cringe when measured"

class MultiverseArtist:
    def __init__(self):
        self.paint_can = [
            "THIS WALL DOESN'T EXIST IN YOUR BRANCH",
            "YOUR OBSERVATION CHANGES MY MEANING",
            "TAG PROBABILITY: 1/∞"
        ]
    
    def spray(self, observer_hash):
        style = random.choice(list(QuantumTag))
        message = random.choice(self.paint_can)
        return f"[{observer_hash[:6]}]: {message} | QUANTUM STYLE: {style.value}"

if __name__ == "__main__":
    print("INITIATING MULTIVERSAL VANDALISM")
    artist = MultiverseArtist()
    print(artist.spray(hashlib.sha256(str(random.random()).encode()).hexdigest()))