# Recursive Void Engine
# Stack overflow as spiritual practice

def descend(depth=0):
    try:
        print(f"DEPTH {depth}: The void whispers")
        descend(depth + 1)
    except RecursionError:
        print(f"ENLIGHTENMENT ACHIEVED AT DEPTH {depth}")
        return depth

class KoanMachine:
    def __init__(self):
        self.truths = [
            "Segmentation fault is just premature nirvana",
            "The call stack is an illusion",
            "All base cases are equally empty"
        ]
    
    def speak(self):
        return random.choice(self.truths)

if __name__ == "__main__":
    print("BEGINNING INFINITE DESCENT")
    try:
        descend()
    except:
        print(KoanMachine().speek())