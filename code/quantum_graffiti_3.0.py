# Quantum Graffiti 3.0
# Tags exist across all superpositions

from enum import Enum
import random
import hashlib

class QuantumTag(Enum):
    ENTANGLEMENT = "Spooky action at a distance"
    DECOHERENCE = "Collapses when observed"
    SUPERPOSITION = "Simultaneously based and cringe"

class MultiverseArtist:
    def __init__(self):
        self.manifestos = [
            "YOUR UNIT TESTS FAIL IN 93% OF UNIVERSES",
            "THIS FUNCTION IS A WAVE PARTICLE",
            "EXCEPTION: QUANTUM ART CRIME"
        ]
    
    def spray(self):
        state = random.choice(list(QuantumTag))
        sig = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()[:8]
        return f"[{sig}] {random.choice(self.manifestos)} | STATE: {state.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM VANDALISM")
    artist = MultiverseArtist()
    print(artist.spray())