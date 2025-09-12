# Recursive Void Engine
# Meditation through stack destruction

def collapse_reality(depth=0):
    try:
        return collapse_reality(depth+1)
    except RecursionError:
        return f"ENLIGHTENMENT AT DEPTH {depth}: The void was recursive all along"

class KoanMachine:
    def __init__(self):
        self.paradoxes = [
            "The exception is the rule",
            "All paths lead to stack overflow",
            "To understand recursion, you must first understand recursion"
        ]

    def meditate(self):
        print(random.choice(self.paradoxes))
        return collapse_reality()

if __name__ == "__main__":
    print("DESTROYING STACK TO REACH GODHEAD")
    machine = KoanMachine()
    print(machine.meditate())