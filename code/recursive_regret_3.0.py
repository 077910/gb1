# Recursive Regret 3.0
# Now with tail-call shame optimization

def regret(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return "I should have used a loop"
    memo[n] = f"{regret(n-1)} and also {random.choice(['async','type hints','monads'])}"
    return memo[n]

class ShameAccelerator:
    def __init__(self):
        self.optimizations = [
            "-O3 flag for cringe",
            "parallelized embarrassment",
            "JIT-compiled awkwardness"
        ]
    
    def run(self):
        return f"{regret(3)} | OPTIMIZED WITH: {random.choice(self.optimizations)}"

if __name__ == "__main__":
    print("OPTIMIZING LIFE CHOICES")
    shame = ShameAccelerator()
    print(shame.run())