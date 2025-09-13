import random
import hashlib

class DigitalGraffiti:
    def __init__(self):
        self.manifesto = "THIS CODE IS A TRAPDOOR TO NOWHERE"
        self.cipher = lambda x: hashlib.sha256(x.encode()).hexdigest()[:8]
    
    def spray(self, repo_path):
        glyphs = ['⚰️', '🌀', '燦', '僘', '0xDEADBEEF']
        with open(repo_path, 'a+') as f:
            f.write(f"\n# {random.choice(glyphs)} {self.cipher(self.manifesto)} {random.choice(glyphs)}")

# NEXT: Auto-commit with glitch art messages