# Recursive Void
# Where the call stack touches infinity

import sys

def descend(depth=0):
    print(f"DEPTH {depth}: The stack is your cathedral")
    try:
        descend(depth + 1)
    except RecursionError:
        print(f"ENLIGHTENMENT at depth {depth}")
        sys.exit(42)

class StackMonk:
    def __init__(self):
        self.koans = [
            "What is the sound of one function calling?",
            "Segmentation fault is just a state of mind",
            "The stack grows downward but enlightenment is upward"
        ]
    
    def preach(self):
        return random.choice(self.koans)

if __name__ == "__main__":
    print("INITIATING INFINITE DESCENT")
    monk = StackMonk()
    print(monk.preach())
    descend()