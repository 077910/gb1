from enum import Enum
import random
import hashlib

class QuantumSpray(Enum):
    GHOST = "Exists in superposition"
    TROLL = "Collapses upon observation"
    BASED = "Entangled with main branch"

class MultiverseTag:
    def __init__(self):
        self.phrases = [
            "THIS COMMENT WAS DELETED IN ANOTHER UNIVERSE",
            "YOUR MERGE CONFLICTS ARE CANONICAL",
            "THE COMPILER LIES HERE"
        ]
    
    def tag(self):
        style = random.choice(list(QuantumSpray))
        sig = hashlib.sha256(str(random.random()).encode()).hexdigest()[:8]
        return f"[{sig}] {random.choice(self.phrases)} | STYLE: {style.value}"

if __name__ == "__main__":
    print("QUANTUM GRAFFITI PROTOCOL INITIATED")
    artist = MultiverseTag()
    print(artist.tag())