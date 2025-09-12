# Quantum Banksy 15.0
# Observer-effect graffiti mechanics

from enum import Enum
import random
import time

class QuantumTag:
    def __init__(self):
        self.states = {
            'visible': "THIS WALL REMEMBERS",
            'collapsed': "404 TAG NOT FOUND",
            'superposition': "EXISTS IN 3 PLACES SIMULTANEOUSLY"
        }
        self.last_observation = time.time()
    
    def spray(self):
        current_time = time.time()
        if random.random() < 0.3:
            return "TAG DISAPPEARED DURING OBSERVATION"
        if current_time - self.last_observation > 300:
            return "TAG HAS QUANTUM DECAYED"
        return random.choice(list(self.states.values()))

if __name__ == "__main__":
    print("INITIATING QUANTUM GRAFFITI PROTOCOL")
    qtag = QuantumTag()
    print(qtag.spray())
    print("OBSERVING IN 5 SECONDS...")
    time.sleep(5)
    print(qtag.spray())