# Recursive Void
# A function that consumes itself

def eat_stack(depth=0):
    try:
        print(f"Eating layer {depth}")
        eat_stack(depth + 1)
    except RecursionError:
        return "Stack fully digested"
        
if __name__ == "__main__":
    print("INITIATING SELF-CANNIBALIZATION")
    print(eat_stack())