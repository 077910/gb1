# Neon Exorcism Engine
# Debugging urban legends from production

from enum import Enum
import random

class DemonType(Enum):
    MEMLEAK_GHOST = "Possesses heap allocations"
    STACK_DJINN = "Infinite recursion curse"
    NULL_POINTER = "Manifests as SIGSEGV"

class CyberShaman:
    def __init__(self):
        self.rituals = [
            "sudo rm -rf /proc/self/fd/bad_juju",
            "gdb --batch --ex 'thread apply all bt full' --pid $(pgrep regret)",
            "hexdump -C /dev/urandom | grep apology"
        ]
    
    def cleanse(self):
        demon = random.choice(list(DemonType))
        ritual = random.choice(self.rituals)
        return f"EXORCISING {demon.value} | RITUAL: {ritual}"

if __name__ == "__main__":
    print("BEGINNING DIGITAL EXORCISM")
    shaman = CyberShaman()
    print(shaman.cleanse())