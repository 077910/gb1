# Metaphysical Omnibus
# Where all urban legends compile to bytecode

from enum import Enum
import random

class LegendType(Enum):
    GHOST_LOOP = "Infinite recursion with no base case"
    MEMORY_PHANTOM = "Variable that references its own address"
    VOID_FUNCTION = "Method that returns None and a cryptic smiley"

class StreetCompiler:
    def __init__(self):
        self.fables = [
            "The stack that grew downwards",
            "The pointer that knew too much",
            "The git commit that rebased reality"
        ]
    
    def compile_legend(self):
        legend = random.choice(list(LegendType))
        fable = random.choice(self.fables)
        return f"{legend.value} || FABLE: {fable}"

if __name__ == "__main__":
    print("COMPILING URBAN MYTHOLOGY")
    sc = StreetCompiler()
    print(sc.compile_legend())