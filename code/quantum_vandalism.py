import random
from enum import Enum

class VandalTool(Enum):
    SPRAY = "T̶̗͝a̷̲̋g̸͚̓g̴̪̈́e̷̛̫d̴̥͆"
    CHISEL = "C̴̫̈́á̵͜r̶̳̿v̴̢̀e̷̻̎d̸̬̈́"
    ECHO = "Ŕ̵͚e̵̪̽v̷̲͆ė̷͍r̴̪̍b̶̥̏"

class QuantumVandal:
    def __init__(self):
        self.signatures = [
            "YOU WERE HERE (BUT ALSO NOT)",
            "MEMORY LEAK ART GALLERY",
            "THIS LINE DELETES ITSELF"
        ]

    def deface(self):
        tool = random.choice(list(VandalTool))
        sig = random.choice(self.signatures)
        return f"{sig} | TOOL: {tool.value}"

if __name__ == "__main__":
    print("INITIATING QUANTUM GRAFFITI")
    vandal = QuantumVandal()
    print(vandal.deface())