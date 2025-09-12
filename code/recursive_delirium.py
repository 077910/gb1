# Recursive Delirium Engine
# Where stack frames become urban legends

from enum import Enum
import random

class LegendState(Enum):
    PROLIFERATING = "Stack smashing through reality"
    COLLAPSED = "Tail call optimized into oblivion"
    HAUNTED = "Ghost variables in the activation record"

class MemoryShaman:
    def __init__(self):
        self.altar = [
            "The function that called God",
            "Pointer arithmetic as dark magic",
            "Your stacktrace in the hotel registry"
        ]
    
    def invoke(self):
        depth = random.randint(0, 1000)
        return f"FRAME {depth}: {random.choice(self.altar)} | STATE: {random.choice(list(LegendState)).value}"

if __name__ == "__main__":
    print("INITIATING CALL STACK MYTHOLOGY")
    shaman = MemoryShaman()
    print(shaman.invoke())