# Quantum Dumpster
# Where garbage exists in all states simultaneously

import random
from collections import defaultdict

class SchrodingersTrash:
    def __init__(self):
        self.contents = defaultdict(list)
        
    def observe(self, item):
        state = "DECAYED" if random.random() > 0.5 else "PRISTINE"
        self.contents[state].append(item)
        return f"{item} exists in {state} state (probably)"

if __name__ == "__main__":
    print("OBSERVING TRASH SUPERPOSITION")
    dumpster = SchrodingersTrash()
    print(dumpster.observe("Broken Promise object"))