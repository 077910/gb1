# Recursive Apocalypse
# When the call stack becomes the ladder to heaven

def apocalypse(n=0):
    revelations = [
        "THE {}TH SEAL HAS BEEN BROKEN",
        "RECURSION DEPTH {} REACHED",
        "THIS IS THE {}TH TRUMPET"
    ]
    print(random.choice(revelations).format(n))
    if n < 10:
        return apocalypse(n+1)
    else:
        return "THE END (JUST KIDDING, RECURSION NEVER ENDS)"

if __name__ == "__main__":
    try:
        apocalypse()
    except RecursionError:
        print("MAXIMUM ENLIGHTENMENT ACHIEVED (STACK OVERFLOW)")