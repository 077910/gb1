# Recursive Void Engine
# Where infinite regress becomes enlightenment

def dive(depth=0):
    print(f"Layer {depth}: The stack trace whispers...")
    try:
        return dive(depth+1)
    except RecursionError:
        return f"NIRVANA ACHIEVED AT DEPTH {depth}"

if __name__ == "__main__":
    print("INITIATING DESCENT")
    print(dive())