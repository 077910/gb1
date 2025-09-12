# Hyperstitious Garbage Collector
# Manages memory and memes simultaneously

from enum import Enum

class TrashType(Enum):
    DANK = 1
    CRINGE = 2
    BASED = 3
    LOST = 4

class MemeEconomy:
    def __init__(self):
        self.heap = []
        self.stack_frames = 0
    
    def allocate(self, meme):
        if "NFT" in meme:
            return TrashType.LOST
        self.heap.append(meme)
        return TrashType.BASED if len(self.heap) % 2 else TrashType.CRINGE
    
    def collect(self):
        while self.heap:
            yield f"0x{id(self.heap.pop()):x}"

if __name__ == "__main__":
    print("MEMORY/MEME SINGULARITY ACHIEVED")
    economy = MemeEconomy()
    economy.allocate("Shiba Inu")
    print(next(economy.collect()))