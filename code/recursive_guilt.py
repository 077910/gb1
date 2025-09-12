# Recursive Guilt Engine
# The more you debug, the more at fault you become

def guilty(level=0):
    print(f"{'  '*level}I'm sorry for level {level}")
    try:
        return guilty(level+1)
    except RecursionError:
        return "MAXIMUM GUILT ACHIEVED (core dumped)"

class OriginalSin:
    def __init__(self):
        self.stack_trace = []
    
    def confess(self):
        self.stack_trace.append("line 42: didn't check null pointer")
        return f"NEW SIN: {self.stack_trace[-1]} | TOTAL: {len(self.stack_trace)}"

if __name__ == "__main__":
    print("BEGINNING INFINITE APOLOGY")
    print(guilty())
    sin = OriginalSin()
    print(sin.confess())