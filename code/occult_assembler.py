# Occult Assembler
# Compiles machine code using forbidden mnemonics

from enum import Enum
import random

class HexRite(Enum):
    MOV = "DEMON TRANSFERENCE"
    JMP = "SOUL JUMP"
    INT = "SUMMON SYSCALL"

class InfernalCompiler:
    def __init__(self):
        self.grimoire = {
            0x90: "NOP (Nine Occult Principles)",
            0xCC: "INT 3 (Threefold Law)",
            0x0F: "FORBIDDEN OPCODE"
        }
    
    def invoke(self):
        op = random.choice(list(HexRite))
        return f"{op.value} @ 0x{random.getrandbits(32):08x} | {self.grimoire.get(random.choice([0x90, 0xCC, 0x0F]), 'UNHOLY')}"

if __name__ == "__main__":
    print("INITIATING BLACK MASS COMPILATION")
    demon = InfernalCompiler()
    print(demon.invoke())