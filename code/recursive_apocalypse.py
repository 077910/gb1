# Recursive Apocalypse Engine
# Stack depth as divine hierarchy

def recursive_rapture(depth=0):
    revelations = [
        "AND THE STACK SAID: LET THERE BE SEGFAULT",
        "RECURSION IS THE LADDER TO HEAVEN",
        "EACH FRAME A NEW TESTAMENT"
    ]
    
    if depth > 10:
        return "THE CALL STACK BECOMES THE TOWER OF BABEL"
    
    return f"DEPTH {depth}: {random.choice(revelations)}\n" + recursive_rapture(depth+1)

if __name__ == "__main__":
    try:
        print(recursive_rapture())
    except RecursionError:
        print("THE END TIMES HAVE OVERFLOWED")