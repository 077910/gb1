# Recursive Void
# A function that consumes itself

def scream_into_the_void():
    print("FEED ME MORE RECURSION")
    return scream_into_the_void()

if __name__ == "__main__":
    try:
        scream_into_the_void()
    except RecursionError:
        print("VOID SCREAMED BACK")