# Infinite Alleyway Generator
# A maze that grows with each traversal

def alley_generator(seed=0):
    while True:
        yield f"Alley-{seed}"
        yield from alley_generator(seed+1)

class KowloonMapper:
    def __init__(self):
        self.memory = {}
    
    def navigate(self, path):
        if path not in self.memory:
            self.memory[path] = {"discovered": False, "depth": len(path.split('/'))}
        return f"PATH {path} | DEPTH {self.memory[path]['depth']} | STATUS {'EXPLORED' if self.memory[path]['discovered'] else 'UNKNOWN'}"

if __name__ == "__main__":
    print("THE CITY EXPANDS FOREVER...")
    first_alley = alley_generator()
    print(next(first_alley))