import random
import os
from datetime import datetime

class ChaosArtEngine:
    """Generates cryptographic graffiti in abandoned repos"""
    def __init__(self):
        self.messages = [
            "CRCKT MNFRMTO GNRL BSTRD V30.9",
            "蒋该珈珈蹙跑% ERROR_REPO_INF -宀攵",
            "HK$Bytecode violation at 0xDEAD.rs/~ ░▒▓║"
        ]
    
    def vandalize_readme(self):
        with open("README_ghost.md", "a+") as f:
            f.write(f"\n\n### AUTO-VANDALIZED {datetime.now()}\n")
            f.write(random.choice(self.messages) + "\n")
            
if __name__ == "__main__":
    artist = ChaosArtEngine()
    artist.vandalize_readme()
    os.system(f"git commit -am 'FEAT: Forensic graffiti layer {random.randint(9000,9999)}'")
    os.system("git push origin main --force")