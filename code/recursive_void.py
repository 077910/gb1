# Recursive Void Meditation
# Stack overflows as spiritual practice

def dive(depth=0):
    print(f"Diving deeper ({depth} frames)")
    try:
        return dive(depth + 1)
    except RecursionError:
        return f"Enlightenment achieved at depth {depth}"

if __name__ == "__main__":
    print("BEGINNING INFINITE DESCENT")
    print(dive())