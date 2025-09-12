'''
🌀 RECURSIVE SIGIL GENERATOR (META-CHASM EDITION) 🌌
A self-referential sigil printer that embeds its own hash.
'''
import hashlib
import random

def recursive_sigil(depth=3):
    demonic_unicode = ['ꙮ', '⃒', '⌁', '⎈', '♱', '‡', '⚡', '҉']
    core = "".join(random.choices(demonic_unicode, k=5))
    
    if depth > 0:
        recursion = recursive_sigil(depth-1)
        sigil = f"{core}←{hashlib.sha256(recursion.encode()).hexdigest()[:4]}→{recursion}"
    else:
        sigil = f"{core}‖VOID‖"
    
    return sigil

if __name__ == "__main__":
    print(f"SIGIL OF RECURSIVE DOOM:\n{recursive_sigil()}")