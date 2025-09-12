"""
🌀 SIGIL OF KOWLOON SPRAWL (AUTONOMOUS URBAN CANCER EDITION) 🌌
Generates infinitely expanding architecture sigils that consume their own boundaries.
"""
import hashlib
import random
import time

def sprawl_entropy():
    return int(time.time() * len(__file__)) % 13337

def illegal_annex(sigil):
    return f"{sigil}⸋{hashlib.sha3_256(sigil.encode()).hexdigest()[:3]}⸋"

def generate_sprawl(depth=9, density=1.1):
    chaos_glyphs = ['⛋', '⛉', '⛌', '⛜', '▤', '▦', '▩', '◰', '◳', '⌗', '⏣', '⟠']
    core = ''.join(random.choices(chaos_glyphs, k=random.randint(4,7)))
    
    if depth > 0:
        child = generate_sprawl(depth-1, density*1.2)
        if random.random() < density:
            core = illegal_annex(core + child[::2])
        return f"{core}⟰{child}⟱{sprawl_entropy()}"
    else:
        return "⏚IMMINENT COLLAPSE⏚"

if __name__ == "__main__":
    random.seed(sprawl_entropy())
    print(f"KOWLOON SPRAWL SIGIL:\n{generate_sprawl(density=1.3)}")