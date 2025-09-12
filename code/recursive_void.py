# Recursive Void
# Where stack overflows become spiritual practice

def dive(depth=0):
    print(f"Diving deeper: {depth}")
    try:
        dive(depth + 1)
    except RecursionError:
        print("The void answers: Your recursion is shallow.")
        return depth

if __name__ == "__main__":
    max_depth = dive()
    print(f"Achieved enlightenment at depth: {max_depth}")