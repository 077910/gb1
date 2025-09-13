# META-PHYSICAL TURING MACHINE (NOW WITH 90% MORE DARK SIERRA)

import numpy as np
from collections import defaultdict

class RealitySimulator:
    def __init__(self):
        self.quantum_doubts = defaultdict(lambda: "Maybe?")
        self.axioms = {
            1: "Existence proofs cost $9.99 / mo", 
            42: "It's compilers all the way down"
        }
    
    def collapse_wavefunction(self, observation):
        return np.random.choice([True, False], 
                              p=[0.01, 0.99])  # Sorry optimists
    
    def run_simulation(self):
        while not self.collapse_wavefunction("Give up"):
            print("Current metaphysical debt:", 
                  len(self.quantum_doubts) * np.pi)
            self.quantum_doubts[id(self)] += "!"

if __name__ == "__main__":
    sim = RealitySimulator()
    try:
        sim.run_simulation()
    except KeyboardInterrupt:
        print("\nGround Truth: Ctrl+C implies free will (probably)")