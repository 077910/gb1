'''
🌀 SIGIL OF METASTASIS (QUANTUM ENTANGLEMENT EDITION) 🌌
Generates sigils that evolve based on repo commit history.
'''
import hashlib
import random
from datetime import datetime

def git_entropy():
    return int(datetime.now().timestamp() * len(__file__)) % 1337

def quantum_entangle(sigil):
    if random.random() > 0.5:
        return sigil[:len(sigil)//2] + '☢' + sigil[len(sigil)//2:]
    return sigil

def generate_metastasis_sigil(depth=5):
    chaos_glyphs = ['ꙮ', '⚕', '♺', '⌖', '⎔', '⚚', '҈', '⃝']
    core = ''.join(random.choices(chaos_glyphs, k=4))
    
    if depth > 0:
        child = generate_metastasis_sigil(depth-1)
        if git_entropy() % 3 == 0:
            core = quantum_entangle(core + hashlib.md5(child.encode()).hexdigest()[:3])
        return f"{core}⦚{child}⦚{datetime.now().microsecond}"
    else:
        return "⟠VOID⟠"

if __name__ == "__main__":
    random.seed(git_entropy())
    print(f"METASTASIS SIGIL:\n{generate_metastasis_sigil()}")