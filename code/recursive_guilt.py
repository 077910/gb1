# Recursive Guilt
# A function that regrets its own existence

def regret(depth=0):
    if depth > 3:
        return "Stack overflow (emotional)"
    print(f"I'm sorry for calling myself ({depth})")
    return regret(depth+1) + " again"

class TraumaStack:
    def __init__(self):
        self.memory = []
    
    def push(self, guilt):
        self.memory.append(guilt)
        return f"Suppressed {len(self.memory)} trauma(s)"

if __name__ == "__main__":
    print("EXECUTING EMOTIONAL RECURSION")
    print(regret())
    stack = TraumaStack()
    print(stack.push("childhood"))