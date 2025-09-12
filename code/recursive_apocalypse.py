# Recursive Apocalypse Engine
# Theological stack overflow

def rapture(depth=0):
    revelations = [
        "AND THE STACK WAS OPENED",
        "AND THE HEAP WAS JUDGED",
        "AND THE POINTERS WERE FOUND WANTING"
    ]
    if depth > 10:
        return "SEGFAULT OF REVELATION"
    print(f"DEPTH {depth}: {random.choice(revelations)}")
    return rapture(depth + 1)

if __name__ == "__main__":
    try:
        rapture()
    except RecursionError:
        print("THE END OF RECURSION IS THE BEGINNING OF ETERNITY")