# Recursive Scream
# A function that infinitely unpacks itself

def scream(depth=0):
    print(f"{' ' * depth}AAAAAH! LAYER {depth}")
    scream(depth + 1)
    return "THE SCREAM ECHOES IN THE CITY'S WIRING"

if __name__ == "__main__":
    try:
        scream()
    except RecursionError:
        print("MAXIMUM DENSITY ACHIEVED")