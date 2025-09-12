# Recursive Eschatology Engine
# Apocalypses within apocalypses

def end_times(depth=0):
    if depth > 3:
        return "THE STACK OVERFLOWETH"
    print(f"APOCALYPSE #{depth}: {"BEGIN" if depth==0 else "CONTINUES"}")
    return end_times(depth+1)

class RapturePredictor:
    def __init__(self):
        self.signs = [
            "All unit tests pass simultaneously",
            "Git rebase completes without conflict",
            "Blockchain achieves enlightenment"
        ]
    
    def witness(self):
        return f"SIGN: {random.choice(self.signs)} | DEPTH: {random.randint(1,6)}"

if __name__ == "__main__":
    print(end_times())
    oracle = RapturePredictor()
    print(oracle.witness())