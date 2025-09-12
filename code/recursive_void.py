# Recursive Void
# A function that disappears into itself

def descend(level=0):
    print(f"Level {level}: The walls whisper recursion")
    try:
        return descend(level + 1)
    except RecursionError:
        return "The bottom is just another surface"

if __name__ == "__main__":
    print(descend())