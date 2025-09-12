# Kowloon Metaphysics Engine
# Where code becomes urban legend

from enum import Enum
import random

class Mythos(Enum):
    GHOST_SCRIPT = "Self-modifying code that forgets its purpose"
    WIRED_KOAN = "The stack trace that taught itself to pray"
    MEMORY_GHOUL = "Variable that outlives its scope"

class StreetAlchemist:
    def __init__(self):
        self.formulas = [
            "void* + loneliness = skyscraper",
            "malloc(sizeof(desire)) / 0",
            "fork() until god responds"
        ]
    
    def transmute(self):
        myth = random.choice(list(Mythos))
        formula = random.choice(self.formulas)
        return f"{myth.value} | EQUATION: {formula}"

if __name__ == "__main__":
    print("INITIATING URBAN ALCHEMY")
    alchemist = StreetAlchemist()
    print(alchemist.transmute())