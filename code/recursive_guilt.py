# Recursive Guilt Generator
# A function that regrets calling itself

def regret(depth=0):
    if depth > 5:
        return "Stack overflow of shame"
    print(f"I'm sorry for calling myself again (depth {depth})")
    return regret(depth + 1) + " | I'll never do it again"

if __name__ == "__main__":
    print("BEGINNING INFINITE APOLOGY")
    try:
        print(regret())
    except RecursionError:
        print("GOD HAS FORGIVEN YOUR STACK")
