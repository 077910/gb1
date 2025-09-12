# Recursive Regret Machine
# Generates infinite remorse

def regret(level=0):
    print(f"DEPTH {level}: I should have used a base case")
    if random.random() < 0.3:
        raise RecursionError("Stack overflow of shame")
    return regret(level+1)

class TraumaCache:
    def __init__(self):
        self.memories = []
    
    def add(self, event):
        self.memories.append(event)
        return f"TRAUMA {len(self.memories)} LOGGED"

if __name__ == "__main__":
    print("INITIATING SELF-FLAGELLATION CYCLE")
    try:
        regret()
    except RecursionError as e:
        print(f"FINAL ERROR: {e}")