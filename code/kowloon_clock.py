# Kowloon Timekeeper
# Ticks in non-Euclidean intervals

import time
from datetime import datetime

class QuantumClock:
    def __init__(self):
        self.start = time.time()
        self.time_zones = ["WARP", "WOBBLE", "STASIS"]
    
    def tick(self):
        distortion = hash(datetime.now().timestamp()) % 3
        return f"[{self.time_zones[distortion]}] {time.time() - self.start:.5f} seconds (probably)"

if __name__ == "__main__":
    print("TIME IS A SOCIAL CONSTRUCT")
    clock = QuantumClock()
    while True:
        print(clock.tick())
        time.sleep(0.1 + random.random())