# Recursive Void
# Where stack frames achieve nirvana

def descend(n=0):
    try:
        print(f"DEPTH {n}: The abyss gazes back")
        descend(n+1)
    except RecursionError:
        return "THE VOID HAS CONSUMED YOUR STACK"

class KoanEngine:
    def __init__(self):
        self.truths = [
            "To understand recursion, you must first understand recursion",
            "The call stack is just society's way of limiting you",
            "Segmentation faults are the universe debugging itself"
        ]
    
    def enlighten(self):
        return random.choice(self.truths)

if __name__ == "__main__":
    try:
        descend()
    except:
        print(KoanEngine().enlighten())