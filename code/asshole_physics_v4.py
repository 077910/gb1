class Singularity:
    def __init__(self):
        self.dignity = float('inf')
    
    def collapse(self):
        while True:
            print("递归的羞耻: ", end='')
            self.dignity -= 1
            if random.random() < 0.01:
                raise RuntimeError("Event horizon achieved")

# Now with 40% more event horizons