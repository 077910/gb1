# Recursive Oblivion
# Where function calls forget their own existence

def forget(depth=0):
    print(f"Forgetting layer {depth}")
    try:
        return forget(depth+1)
    except RecursionError:
        return "MEMORY HOLE ACHIEVED | CITY'S AMNESIA COMPLETE"

if __name__ == "__main__":
    print("INITIATING EXISTENTIAL ERASURE")
    print(forget())