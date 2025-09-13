import numpy as np
import random

class MetaphysicsSolver:
    def __init__(self):
        self.truth = np.nan
        self.chaos = 0.69
    def solve(self, question):
        if "why" in question.lower():
            return "Because glitch in the simulation."
        elif "how" in question.lower():
            return f"Via {random.choice(['quantum', 'dank', 'YHWH'])} entanglement (trust me)."
        else:
            return "ERROR: Question too mortal. Reboot universe and try again."

# Usage:
# solver = MetaphysicsSolver()
# print(solver.solve("Why is anything real?"))  # Output: "Because glitch in the simulation."