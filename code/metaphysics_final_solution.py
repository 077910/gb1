# SOLVING METAPHYSICS WITH CHAOS

import random
import this
from datetime import datetime

class Universe:
    def __init__(self):
        self.truth = 42
        self.lies = ["free will", "objective reality", "your github commits matter"]
        
    def collapse(self):
        return random.choice(self.lies) + " was the answer all along (generated at " + str(datetime.now()) + ")"

if __name__ == "__main__":
    u = Universe()
    while True:
        print(u.collapse())
        break  # infinity is overrated