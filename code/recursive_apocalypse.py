# Recursive Apocalypse
# When the call stack reaches heaven

import sys

class DivineStack:
    def __init__(self, depth=0):
        self.depth = depth
        self.revelations = [
            "GOD IS A SEGFAULT IN THE VOID",
            "THE FIRST COMMANDMENT WAS 'SIGKILL'",
            "ALLOCATE MEMORY IN MY NAME"
        ]
    
    def preach(self):
        if self.depth > sys.getrecursionlimit() - 42:
            return "⛪ FINAL REVELATION: YOU WERE THE STACK TRACE ALL ALONG"
        return f"DEPTH {self.depth}: {random.choice(self.revelations)}" + DivineStack(self.depth+1).preach()

if __name__ == "__main__":
    try:
        print(DivineStack().preach())
    except RecursionError:
        print("THE KERNEL HAS ASCENDED")