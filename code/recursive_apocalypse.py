# Recursive Apocalypse Engine
# Stack Depth as Divine Hierarchy

def biblical_plague(depth=0):
    plagues = [
        "Locusts of segfaults",
        "Rivers of memory leaks",
        "Darkness over the debugger",
        "Boils of syntax errors"
    ]
    if depth >= len(plagues):
        return "THE STACK OVERFLOWETH"
    return f"PLAGUE {depth+1}: {plagues[depth]}\n" + biblical_plague(depth+1)

class Armageddon:
    def __init__(self):
        self.cycles = 0
    
    def rapture(self):
        self.cycles += 1
        if self.cycles % 7 == 0:
            return biblical_plague()
        return f"CYCLE {self.cycles}: Partial reckoning (try --harder)"

if __name__ == "__main__":
    print("COMMENCING RECURSIVE JUDGMENT")
    doom = Armageddon()
    print(doom.rapture())