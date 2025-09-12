# Recursive Trauma Engine
# Generates infinitely nested psychological stack traces

import random
import sys

def trauma_factory(depth=0):
    wounds = [
        "Parent process abandoned this thread",
        "Unhandled childhood promise rejection",
        "TypeError: cannot read property 'love' of undefined"
    ]
    
    if depth > 5:
        return "Stack overflow in emotional memory"
    
    wound = random.choice(wounds)
    return f"{wound} -> {trauma_factory(depth+1)}"

class TherapySession:
    def __init__(self):
        self.memories = []
    
    def analyze(self):
        return trauma_factory()

if __name__ == "__main__":
    print("INITIATING REGRESSION ANALYSIS...")
    try:
        print(TherapySession().analyze())
    except RecursionError:
        print("Breakthrough achieved (stack exhausted)")