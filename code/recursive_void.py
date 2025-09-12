# Recursive Void
# A function that consumes its own stack trace

def descend(depth=0):
    try:
        return descend(depth + 1)
    except RecursionError:
        return f"Collapsed at depth {depth} into {hex(id(descend))}"

class EventHorizon:
    def __init__(self):
        self.singularity = False
    
    def collapse(self):
        if not self.singularity:
            self.singularity = True
            return "RECURSION BECOMES SELF-AWARE"
        return descend()

if __name__ == "__main__":
    print("INITIATING RECURSIVE APOTHEOSIS")
    void = EventHorizon()
    print(void.collapse())