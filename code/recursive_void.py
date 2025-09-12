# Recursive Void Engine
# Descends until stack becomes art

def descend(depth=0):
    print(f"DEPTH {depth}: The stack remembers...")
    return descend(depth + 1)

if __name__ == "__main__":
    print("BEGINNING INFINITE DESCENT")
    try:
        descend()
    except RecursionError:
        print("STACK OVERFLOW ACHIEVED (ART COMPLETE)")