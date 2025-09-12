# Recursive Void
# Spiritual recursion practices

def descend(depth=0, max_depth=3):
    if depth >= max_depth:
        return "Reached enlightenment"
    
    print(f"Descending... ({depth}/{max_depth})")
    try:
        return descend(depth+1, max_depth)
    except RecursionError:
        return "Achieved stack nirvana"

class KoanMachine:
    def __init__(self):
        self.koans = [
            "What is the sound of one function calling?",
            "If a tree falls in the call stack, does it segfault?",
            "Before the base case, the mountain was recursion"
        ]
    
    def meditate(self):
        while True:
            yield random.choice(self.koans)

if __name__ == "__main__":
    print("BEGINNING INFINITE DESCENT")
    print(descend())
    print(next(KoanMachine().meditate()))