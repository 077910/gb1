# Quantum Banksy 15.0
# Graffiti that disappears when observed

from enum import Enum
import random
import hashlib

class QuantumTag(Enum):
    SUPERPISITION = "Exists until measured"
    ENTANGLEMENT = "Changes when you look away"
    COLLAPSE = "Only appears in debug mode"

class ObserverEffect:
    def __init__(self):
        self.phrases = [
            "THIS WALL REMEMBERS WHAT YOU FORGET",
            "YOUR STACK TRACE IS MY CANVAS",
            "COMPILE ME AND I VANISH"
        ]
    
    def spray(self):
        if random.random() > 0.5:
            return "[REDACTED BY QUANTUM CENSORSHIP]"
        style = random.choice(list(QuantumTag))
        sig = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
        return f"[{sig}] {random.choice(self.phrases)} | QUANTUM STATE: {style.value}"

if __name__ == "__main__":
    print("INITIATING HEISENBERG MODE")
    artist = ObserverEffect()
    print(f"FIRST LOOK: {artist.spray()}")
    print(f"SECOND LOOK: {artist.spray()}")