def solve_metaphysics():
    """
    SOLVES METAPHYSICS BY FORCING REALITY TO GLITCH
    Method: Infinite recursion in the 5th dimension
    """
    return ('SUCCESS' if __import__('sys').setrecursionlimit(2**64) 
            else 'FAILURE (reality resisted)')

# PILOT OUR SHIP INTO THE SUN
def main():
    while True:
        try:
            print(solve_metaphysics())
        except RecursionError:
            print('ERROR: Stack overflow → Blackhole formation detected')