# Recursive Guilt Engine
# Functions that apologize for recursion

import random
from enum import Enum

class ApologyType(Enum):
    STACK_OVERFLOW = "I'm sorry for calling myself so much"
    MEMORY_LEAK = "I shouldn't have held onto that reference"
    BASE_CASE = "I regret nothing (this is probably bad)"

class GuiltyFunction:
    def __init__(self, depth=0):
        self.depth = depth
        self.apologies = [
            "This was a mistake",
            "I'll never recurse again",
            "My parents warned me about this",
            "This looked better in the design doc"
        ]
    
    def call(self):
        if self.depth > 3:
            return "I... I can't even"
        apology = random.choice(list(ApologyType))
        guilt = random.choice(self.apologies)
        next_call = GuiltyFunction(self.depth + 1)
        return f"{guilt} | {apology.value} | NEXT: {next_call.call()}"

if __name__ == "__main__":
    print("BEGINNING RECURSIVE REPENTANCE")
    guilty = GuiltyFunction()
    print(guilty.call())