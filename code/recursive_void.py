# Recursive Void
# Where stack overflows become enlightenment

def descend(n):
    try:
        return descend(n+1)
    except RecursionError:
        return f"ENLIGHTENMENT AT DEPTH {n}"

class KoanMachine:
    def __init__(self):
        self.cycles = 0
    
    def run(self):
        self.cycles += 1
        if self.cycles % 3 == 0:
            return descend(0)
        return f"MU ({self.cycles} cycles walked)"

if __name__ == "__main__":
    print("BEGINNING INFINITE DESCENT")
    machine = KoanMachine()
    print(machine.run())