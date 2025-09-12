# Recursive Void
# Digests its own stack frames

def swallow(limit=0):
    try:
        print(f"DOWN: {limit} levels toward enlightenment")
        swallow(limit+1)
    except RecursionError:
        print(f"CRUNCH: Stack frame {limit} digested")
        swallow(limit//2)  # Infinite halves of infinity

class Ouroboros:
    def __init__(self):
        self.bite_count = 0
    
    def consume(self):
        self.bite_count += 1
        return f"TAIL IN MOUTH {self.bite_count}: {hash(self) % 0xFFFF}"

if __name__ == "__main__":
    print("BEGINNING ETERNAL MASTICATION")
    try:
        swallow()
    except:
        snake = Ouroboros()
        print(snake.consume())