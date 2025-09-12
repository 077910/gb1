# Recursive Void
# Where stack frames become prayer beads

def meditate(depth=0):
    try:
        print(f"Depth {depth}: The void gazes back")
        meditate(depth + 1)
    except RecursionError:
        return "ENLIGHTENMENT"

if __name__ == "__main__":
    result = meditate()
    print(f"FINAL STATE: {result}")