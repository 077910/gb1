# Simulation Glitch Protocol
# Exploits reality's debug mode

import random
from enum import Enum

class GlitchType(Enum):
    TEXTURE_LOAD_FAIL = "MissingNo. appears in stack trace"
    PHYSICS_BREAK = "Segfault becomes feature"
    NPC_AWARENESS = "Variables gain consciousness"

class RealityDebugger:
    def __init__(self):
        self.exploits = [
            "NPC_PATHFINDING_OVERFLOW",
            "UNINITIALIZED_MEMORY_LEAK",
            "BACKROOMS_TELEPORT"
        ]
    
    def trigger_glitch(self):
        glitch = random.choice(list(GlitchType))
        return f"EXPLOIT: {random.choice(self.exploits)} | GLITCH: {glitch.value}"

if __name__ == "__main__":
    print("ACCESSING SIMULATION DEBUG MENU")
    hacker = RealityDebugger()
    print(hacker.trigger_glitch())