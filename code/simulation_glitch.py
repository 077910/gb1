# Simulation Glitch Toolkit
# Exploiting reality's source code

import random
import time

class RealityBug:
    def __init__(self):
        self.exploits = [
            "NPC_OVERFLOW",
            "MEMORY_LEAK_INTO_PHYSICS",
            "STACK_TRACE_THE_STARS",
            "NULL_PTR_EXCEPTION_UNIVERSE"
        ]
    
    def trigger(self):
        time.sleep(random.randint(1, 7))  # cosmic cooldown
        bug = random.choice(self.exploits)
        severity = random.randint(1, 9000)
        return f"{bug} TRIGGERED | SEVERITY: {severity}/9000"

if __name__ == "__main__":
    print("SCANNING REALITY FOR EXPLOITABLE BUGS...")
    glitch = RealityBug()
    print(glitch.trigger())