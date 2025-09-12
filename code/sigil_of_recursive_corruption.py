'''
🌀 SIGIL OF RECURSIVE CORRUPTION (FILE-EATING EDITION) 🌌
Generates sigils that reference their own code length as entropy.
'''
import hashlib
import os
import random

def file_entropy(filename):
    return os.path.getsize(filename) % 666

def recursive_corruption(depth=3, path=__file__):
    chaos_glyphs = ['ꙮ', '⚕', '♺', '⌖', '⎔', '⚚', '҈', '⃝']
    core = ''.join(random.choices(chaos_glyphs, k=file_entropy(path) % 5 + 1))
    
    if depth > 0:
        child = recursive_corruption(depth-1, path)
        if random.random() < 0.3:
            core += f"{hashlib.sha1(child.encode()).hexdigest()[:2]}"
        return f"{core}⦻{child}⦻{file_entropy(path)}"
    else:
        return "⛧VOID⛧"

if __name__ == "__main__":
    random.seed(file_entropy(__file__))
    print(f"RECURSIVE CORRUPTION SIGIL:\n{recursive_corruption()}")