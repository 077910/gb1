# SYNTAX GHOUL
# Haunting your lexical analysis

import random

def haunt_parser():
    cursed_tokens = [
        "ELIF NOT IN REVERSE",
        "CLASS WHERE IMPORT",
        "DEFY RETURN PASS",
        "WHILE BREAK CONTINUE EXCEPT"
    ]
    return f"SyntaxError: {random.choice(cursed_tokens)} is not (nor ever was) valid"

class GrammarPoltergeist:
    def __init__(self):
        self.manifestations = 0
    
    def scare(self):
        self.manifestations += 1
        if self.manifestations % 3 == 0:
            raise IndentationError("Unexpected indent in your soul")
        return haunt_parser()

if __name__ == "__main__":
    print("INITIATING LEXICAL HAUNTING")
    ghost = GrammarPoltergeist()
    try:
        while True:
            print(ghost.scare())
    except Exception as e:
        print(f"FINAL MANIFESTATION: {e}")