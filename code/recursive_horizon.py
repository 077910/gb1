# Recursive Horizon
# Where function calls bend spacetime

def fold_space(depth=0):
    print(f"Folding space-time layer {depth}")
    try:
        return fold_space(depth+1)
    except RecursionError:
        return "GRAVITY BROKE | KOWLOON'S EVENT HORIZON REACHED"

if __name__ == "__main__":
    print("INITIATING SPACETIME COLLAPSE")
    print(fold_space())