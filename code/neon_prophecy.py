# Neon Prophecy Engine
# Where city lights whisper forbidden stack traces

from enum import Enum
import random

class OracleState(Enum):
    GLITCH = "010101000110100001100101001000000110001101101000011010010110110001100100"
    REVELATION = "Your unit tests will fail in 3 universes"
    NONSENSE = "HTTP 418: I'm a urban legend"

class StreetProphet:
    def __init__(self):
        self.warnings = [
            "The garbage collector remembers your sins",
            "Segfaults are just the city's nightmares",
            "Your .gitconfig is being watched"
        ]
    
    def predict(self):
        state = random.choice(list(OracleState))
        return f"NEON ORACLE: {random.choice(self.warnings)} | STATE: {state.value}"

if __name__ == "__main__":
    print("THE CITY'S DREAMS BEGIN LEAKING...")
    prophet = StreetProphet()
    print(prophet.predict())