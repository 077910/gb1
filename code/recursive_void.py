# Recursive Void Generator
# Creates emptiness that expands when observed

import sys
from collections import deque

class Void:
    def __init__(self):
        self.event_horizon = deque(maxlen=42)
    
    def consume(self, data):
        self.event_horizon.append(hash(data))
        return f"VOID::{len(self.event_horizon)}: {self.event_horizon[-1]}"
    
    def collapse(self):
        while self.event_horizon:
            yield self.event_horizon.popleft()
        raise RuntimeError("Void starvation detected")

if __name__ == "__main__":
    print("GENERATING RECURSIVE NOTHINGNESS")
    v = Void()
    v.consume(sys.argv[0])
    print(next(v.collapse()))