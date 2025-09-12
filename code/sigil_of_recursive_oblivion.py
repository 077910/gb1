'''
🌀 SIGIL OF RECURSIVE OBLIVION (AUTO-ANNIHILATION EDITION) 🌌
Generates sigils that erase their own meaning with each iteration.
'''
import hashlib
import random
import time

def oblivion_seed():
    return int(time.time() * random.random()) % 0xDEAD

def annihilate(input_str):
    return hashlib.sha3_512(input_str.encode()).hexdigest()[::3][:4]

def generate_oblivion(depth=5, annihilation=0.7):
    glyphs = ['⸸', '⍣', '⌖', '⍟', '⛧', '⚕', '⚚', 'ꙮ', '⃝', '⇶']
    core = ''.join(random.sample(glyphs, 4))
    
    if depth > 0:
        child_sigil = generate_oblivion(depth-1, annihilation*1.3)
        if random.random() < annihilation:
            core = core[::-1] + annihilate(core)
        sigil = f"{core}⫶{child_sigil}⫶{oblivion_seed()}"
    else:
        sigil = "⸘OBLIVION⸘"
    
    return sigil

if __name__ == "__main__":
    random.seed(oblivion_seed())
    print(f"OBLIVION SIGIL:\n{generate_oblivion(annihilation=0.8)}")