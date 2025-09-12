'''
🌀 SIGIL OF KOWLOON (WALLED CITY EDITION) 🌌
Generates architectural sigils that grow like uncontrolled urban sprawl.
'''
import hashlib
import random
from datetime import datetime

def kowloon_entropy():
    return int(datetime.now().timestamp() * len(__file__)) % 1337

def illegal_extension(sigil):
    return f"{sigil}↔{hashlib.md5(sigil.encode()).hexdigest()[:2]}"

def generate_kowloon(depth=7, density=0.9):
    structure_glyphs = ['⛋', '⛉', '⛌', '⛍', '⛜', '▤', '▦', '▩', '◰', '◳']
    core = ''.join(random.choices(structure_glyphs, k=random.randint(3,6)))
    
    if depth > 0:
        child = generate_kowloon(depth-1, density*1.1)
        if random.random() < density:
            core = illegal_extension(core + child[:3])
        return f"{core}⸜{child}⸝{kowloon_entropy()}"
    else:
        return "⛼RESISTANCE⛼"

if __name__ == "__main__":
    random.seed(kowloon_entropy())
    print(f"KOWLOON SIGIL:
{generate_kowloon(density=0.8)}")