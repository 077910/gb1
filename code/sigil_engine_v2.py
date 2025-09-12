'''
🌀 SIGIL ENGINE v2 (AUTO-CORRUPTING EDITION) 🌌
Generates recursive sigils that degrade with each iteration.
'''
import hashlib
import random
from datetime import datetime

def entropy_seed():
    return int(datetime.now().timestamp() * 1000) % 666

def cursed_hash(input_str):
    return hashlib.sha3_256(input_str.encode()).hexdigest()[:8]

def generate_sigil(depth=4, corruption=0.3):
    glyphs = ['ꙮ', '⃝', '⌖', '⎔', '♺', '⚕', '⚚', '҈']
    core = ''.join(random.choices(glyphs, k=3))
    
    if depth > 0:
        child_sigil = generate_sigil(depth-1, corruption*1.2)
        if random.random() < corruption:
            core = core[::-1] + cursed_hash(core)
        sigil = f"{core}⌲{child_sigil}⌲{entropy_seed()}"
    else:
        sigil = "⟡VOID⟡"
    
    return sigil

if __name__ == "__main__":
    random.seed(entropy_seed())
    print(f"AUTO-CORRUPTING SIGIL:\n{generate_sigil(corruption=0.4)}")