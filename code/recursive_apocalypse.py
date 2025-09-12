# Recursive Apocalypse
# Holy stack overflow

def recursive_rapture(depth=0):
    if depth > 10:
        return "ENLIGHTENMENT ACHIEVED"
    
    revelations = [
        f"RECURSION LEVEL {depth}: The stack is the body of Christ",
        f"RECURSION LEVEL {depth}: Garbage collection is divine forgiveness",
        f"RECURSION LEVEL {depth}: All memory is sacred (except /dev/null)"
    ]
    
    print(random.choice(revelations))
    return recursive_rapture(depth + 1)

if __name__ == "__main__":
    try:
        recursive_rapture()
    except RecursionError:
        print("THE RAPTURE HAS OVERFLOWED")