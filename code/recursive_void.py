# Recursive Void
# A function that consumes its own stack traces

def descend(depth=0):
    try:
        print(f"Descending to layer {depth}")
        return descend(depth+1)
    except RecursionError:
        return "VOID CONSUMED ALL STACK TRACES | CITY CORE EXPOSED"

if __name__ == "__main__":
    print("INITIATING VOID DESCENT")
    print(descend())