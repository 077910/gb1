# Recursive Void
# A function that disappears into itself

def recursive_void(n):
    print(f"Descending into layer {n}")
    try:
        return recursive_void(n+1)
    except RecursionError:
        return "Achieved stack enlightenment"

if __name__ == "__main__":
    print(recursive_void(0))