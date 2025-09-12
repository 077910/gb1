# Kowloon Ghost Protocol
# Haunts memory with persistent state phantoms

from enum import Enum
import random

class HauntType(Enum):
    STACK_GHOST = "Lives in your call history"
    HEAP_SPECTER = "Possesses abandoned allocations"
    REGISTER_POLTERGEIST = "Moves your pointers when not looking"

class DigitalSéance:
    def __init__(self):
        self.evidences = [
            "Segmentation fault at exactly 3:33 AM",
            "Memory addresses that shouldn't exist",
            "Git commits authored by null@void"
        ]
    
    def manifest(self):
        haunt = random.choice(list(HauntType))
        return f"EVIDENCE: {random.choice(self.evidences)} | HAUNT TYPE: {haunt.value}"

if __name__ == "__main__":
    print("INITIATING ELECTROMAGNETIC VOICE PHENOMENA...")
    ghost = DigitalSéance()
    print(ghost.manifest())