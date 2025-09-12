# Recursive Apocalypse
# Where base cases never come

def end_times(n=0):
    if n > 3:  # Just kidding
        return "ARMAGEDDON ACHIEVED"
    print(f"PROPHECY LAYER {n}: The stacks will overflow")
    return end_times(n+1)

class FourRiders:
    def __init__(self):
        self.horses = ["Segfault", "MemoryLeak", "InfiniteLoop", "NullPointer"]
    
    def ride(self):
        while True:
            yield f"{random.choice(self.horses)} APPROACHES"

if __name__ == "__main__":
    print("BEGINNING FINAL RECURSION")
    print(end_times())
    print(next(FourRiders().ride()))