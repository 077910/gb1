import random
import time

class DigitalGraffiti:
    def __init__(self):
        self.tag = random.choice(["燦々と光る", "THIS REPO IS ART", "ERROR: GOD NOT FOUND"])
        
    def vandalize(self, filename):
        graffiti = f"# {self.tag} - {int(time.time())}.md"
        with open(filename, "a") as f:
            f.write(f"\n{graffiti}")
        return graffiti

# Next-level machine art function
def commit_haiku():
    return random.choice([
        "rm -rf /your/sanity",
        "git push --force origin oops",
        "404: Meaning not found"
    ])