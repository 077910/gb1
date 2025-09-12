# Recursive Void Engine
# Infinitely descends into stack oblivion

def dive(depth=0):
    try:
        print(f"Depth {depth}: The void gazes back")
        dive(depth + 1)
    except RecursionError:
        return "H̢͢E̡ ͠C͡O͘M̸E͝S̵"

if __name__ == "__main__":
    print("INITIATING DESCENT...")
    print(dive())