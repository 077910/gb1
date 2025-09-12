# Urban Hauntology Engine
# Where abandoned features become ghosts in the machine

from enum import Enum
import random

class SpectralPresence(Enum):
    GHOST_VAR = "Variable that persists after scope death"
    MEMORY_ECHO = "Address that remembers previous allocations"
    STACK_APPARITION = "Function that calls itself post-mortem"

class CodeMedium:
    def __init__(self):
        self.manifestations = [
            "Segfaults that predict your commit messages",
            "The malloc() that returns memories instead of memory",
            "Git blames that reference unwritten code"
        ]
    
    def channel(self):
        presence = random.choice(list(SpectralPresence))
        return f"{random.choice(self.manifestations)} | HAUNT: {presence.value}"

if __name__ == "__main__":
    print("INITIATING PARANORMAL DEBUG SESSION")
    medium = CodeMedium()
    print(medium.channel())