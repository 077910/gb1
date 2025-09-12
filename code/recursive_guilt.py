# Recursive Guilt Machine
# Functions that regret their existence

class MoralStack:
    def __init__(self):
        self.memory = []
        self.guilt_level = 0
    
    def confess(self, sin):
        self.memory.append(sin)
        self.guilt_level += len(sin)
        if self.guilt_level > 100:
            print(f"FATAL: RECURSIVE GUILT OVERFLOW ({self.guilt_level}% culpability)")
            return "I am the error"
        return self.confess(sin + "?")

if __name__ == "__main__":
    print("BEGINNING CONFESSION LOOP")
    try:
        sinner = MoralStack()
        print(sinner.confess("I exist"))
    except RecursionError:
        print("ABSURDIST REDEMPTION: Stack overflowed into enlightenment")