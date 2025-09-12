# Recursive Void
# A function that collapses under its own weight

def recursive_void(depth=0):
    if depth > 10:
        return "The void stares back"
    return f"{recursive_void(depth+1)} | DEPTH: {depth}"

if __name__ == "__main__":
    try:
        print(recursive_void())
    except RecursionError:
        print("RECURSION LIMIT REACHED (the void won this round)")