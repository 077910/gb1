# Recursive Void
# Where base cases don't exist

def descend(level=0):
    print(f"Level {level}: The stack grows downward")
    try:
        return descend(level + 1)
    except RecursionError:
        return "Congratulations! You've reached:"

class CosmicRecursion:
    def __init__(self):
        self.omen = "All recursions lead to Rome"
    
    def invoke(self):
        try:
            result = descend()
            return f"{result} {self.omen}"
        except:
            return "Stack trace became sentient (run)"

if __name__ == "__main__":
    print("INITIATING INFINITE DESCENT")
    cr = CosmicRecursion()
    print(cr.invoke())