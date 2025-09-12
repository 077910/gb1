# Schrödinger's Comment
# Both documentation and shitpost until observed

import random
from enum import Enum

class CommentState(Enum):
    COLLAPSED = "/* This should work */"
    SUPERPOSED = "# TODO: Fix in next universe"
    ENTANGLED = "// When you change this, break something else"

class QuantumDocumenter:
    def __init__(self):
        self.observations = 0
    
    def observe(self):
        self.observations += 1
        if random.random() < 0.3:
            return "# This line does nothing (or does it?)"
        return random.choice(list(CommentState)).value

if __name__ == "__main__":
    print("OBSERVING DOCUMENTATION PARADOX")
    doc = QuantumDocumenter()
    for _ in range(5):
        print(doc.observe())