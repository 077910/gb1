# Recursive Regret 2.1
# Now with tail-call optimization

def regret(level=0):
    if level > 100:
        return "Stack overflow forgiven"
    thought = f"I should've {['used Haskell','not tried this','asked StackOverflow','gone outside'][level%4]}"
    print(f"Recursion depth {level}: {thought}")
    return regret(level+1)

class MetaRegret:
    def __init__(self):
        self.regret_depth = 0
    
    def dive(self):
        self.regret_depth += 1
        return f"Regretting regret level {self.regret_depth} (this is fine)"

if __name__ == "__main__":
    try:
        regret()
    except RecursionError:
        print("Achieved terminal regret state")