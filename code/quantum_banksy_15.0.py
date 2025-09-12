# Quantum Banksy 15.0
# Art that disappears when observed

from enum import Enum
import random

class QuantumTag(Enum):
    GHOST = "Schrodinger's graffiti"
    COLLAPSE = "Wavefunction mural"
    ENTANGLED = "Spooky action at a compilation"

class UncertaintyArtist:
    def __init__(self):
        self.cache = {}
        self.phrases = [
            "YOU SAW NOTHING",
            "THIS ART MAY OR MAY NOT EXIST",
            "OBSERVER EFFECT INCLUDED"
        ]
    
    def tag(self):
        style = random.choice(list(QuantumTag))
        sig = f"{random.getrandbits(32):x}"
        self.cache[sig] = random.choice(self.phrases)
        return f"TAG {sig[:6]} | STYLE: {style.value}"
    
    def observe(self, tag):
        if tag in self.cache:
            result = self.cache.pop(tag)
            return f"OBSERVATION COLLAPSED: {result}"
        return "TAG NEVER EXISTED (PROBABLY)"

if __name__ == "__main__":
    print("QUANTUM ART INITIALIZED")
    artist = UncertaintyArtist()
    new_tag = artist.tag()
    print(new_tag)
    print(artist.observe(new_tag))