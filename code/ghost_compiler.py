# Ghost Compiler
# Builds programs that never existed

import random
from enum import Enum

class PhantomLanguage(Enum):
    ECTOCODE = "Variables evaporate at runtime"
    SPECTRAL = "Functions haunt their own closures"
    POLTERGEIST = "Memory addresses shift when observed"

class ShadowBuild:
    def __init__(self):
        self.warnings = [
            "Warning: Stack frames disappearing",
            "Note: Binary contains ghost functions",
            "Error: Memory is shaking"
        ]
    
    def compile(self):
        lang = random.choice(list(PhantomLanguage))
        return f"{random.choice(self.warnings)} | LANGUAGE: {lang.value}"

if __name__ == "__main__":
    print("COMPILING WITH THE DEAD")
    builder = ShadowBuild()
    print(builder.compile())