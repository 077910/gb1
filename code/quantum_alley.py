# Quantum Alleyway
# Where paths exist in superposition until observed

import random
from collections import defaultdict

class QuantumAlley:
    def __init__(self):
        self.possibilities = defaultdict(list)
        
    def add_possibility(self, origin, destination):
        self.possibilities[origin].append(destination)
        
    def traverse(self, current_path):
        if not self.possibilities[current_path]:
            return "DEAD_END"
        next_step = random.choice(self.possibilities[current_path])
        return f"{current_path} → {next_step}"

# The city exists in multiple states simultaneously
if __name__ == "__main__":
    qa = QuantumAlley()
    qa.add_possibility("Alley-0", "Alley-1")
    qa.add_possibility("Alley-0", "Alley-42")
    print(qa.traverse("Alley-0"))