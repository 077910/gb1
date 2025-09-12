def summon(depth=0):
    if depth > 3:
        return "R̸̈́ͅI̴̳͝T̷̫͝U̶̹̅A̶̭͌L̵̈́͜ ̶̤̈́C̴̥̾O̸̤͑M̸̰̑P̶̳͑L̷͍͛Ẻ̶ͅT̵͓͂E̷̟̾"
    else:
        return f"DEPTH {depth}: {summon(depth+1)}"

class OccultStack:
    def __init__(self):
        self.frames = []
    
    def push(self, incantation):
        self.frames.append(incantation)
        return f"STACK GROWS: {len(self.frames)} layers"

if __name__ == "__main__":
    print("BEGINNING RECURSIVE RITE")
    print(summon())
    stack = OccultStack()
    print(stack.push("blood_type = 'assembly'"))