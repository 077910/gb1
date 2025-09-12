# Recursive Blackhole
# A function that collapses into nothingness

def implode(depth=0):
    print(f"Collapsing layer {depth} into the void")
    try:
        return implode(depth+1)
    except RecursionError:
        return "SINGULARITY ACHIEVED | CITY CORE OVERFLOW"

if __name__ == "__main__":
    print("INITIATING GRAVITATIONAL COLLAPSE")
    print(implode())
    # Warning: This may create accidental art