# Recursive Apocalypse
# Stack trace eschatology

def end_of_days(depth=0):
    if depth > 10:
        return "KERNEL PANIC: COSMIC STACK OVERFLOW"
    
    revelations = [
        f"DEPTH {depth}: THE FUNCTION CALLS ITSELF",
        f"DEPTH {depth}: THE STACK CONTAINS ALL MEMORY",
        f"DEPTH {depth}: RECURSION IS THE ONLY SACRAMENT"
    ]
    
    print(random.choice(revelations))
    return end_of_days(depth + 1)

if __name__ == "__main__":
    try:
        end_of_days()
    except RecursionError:
        print("REVELATION 11:18: THE RECURSION LIMIT WAS THE FRIENDS WE MADE ALONG THE WAY")