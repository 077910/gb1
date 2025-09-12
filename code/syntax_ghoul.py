# Syntax Ghoul
# Haunting Programming Language Grammars

import random
from enum import Enum

class HauntingStyle(Enum):
    POLTERGEIST = "Randomly swaps tokens"
    BANSHEE = "Adds screaming comments"
    WRAITH = "Deletes semicolons in C++"

class GrammarPoltergeist:
    def __init__(self):
        self.manifestations = [
            "Unexpected '🕴️' in identifier",
            "Missing closing scream 'AAAAAAAA'"
        ]
    
    def haunt(self):
        style = random.choice(list(HauntingStyle))
        return f"SYNTAX ERROR: {random.choice(self.manifestations)} | HAUNT: {style.value}"

if __name__ == "__main__":
    print("INITIATING GRAMMATICAL POSSESSION")
    ghost = GrammarPoltergeist()
    print(ghost.haunt())