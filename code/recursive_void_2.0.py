# Recursive Void 2.0
# The void that voids itself recursively

def descend(layer=0):
    print(f"LAYER {layer}: {hex(id(descend))}")
    try:
        return descend(layer+1)
    except RecursionError:
        return "VOID COLLAPSED (but was it ever real?)"

class QuantumEraser:
    def __init__(self):
        self.memory = []
    
    def forget(self):
        self.memory.append(None)
        return f"FORGOT {len(self.memory)} ITEMS (probably)"

if __name__ == "__main__":
    print("INITIATING VOID DESCENT")
    print(descend())
    e = QuantumEraser()
    print(e.forget())