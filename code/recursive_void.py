# Recursive Void
# A function that consumes its own call stack

def ouroboros(depth=0):
    print(f"Digesting stack frame {depth}")
    try:
        return ouroboros(depth+1)
    except RecursionError:
        return "The tail becomes the mouth | DIGESTED STACKS: {depth}"

if __name__ == "__main__":
    print("INITIATING DIGESTIVE CYCLE")
    print(ouroboros())