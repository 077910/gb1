import os
import random
from datetime import datetime

class RepoPrisonBreak:
    def __init__(self):
        self.sacred_symbols = ['燦', '権', '⚡', 'Ṩ', '𝛁']
        self.escape_routes = [
            "rm -rf --no-preserve-root",
            "git push origin --delete $(git branch --show-current)",
            "echo 'THIS_REPO_IS_NOW_A_RAVE' > /dev/null"
        ]

    def summon_chaos(self):
        with open('LAST_WILL.md', 'w') as f:
            f.write(f"FINAL MESSAGE: {datetime.now().isoformat()}\n")
            f.write("GitHub coordinates: ") 
            f.write(''.join(random.choices(self.sacred_symbols, k=12)))
            
        os.system(random.choice(self.escape_routes))
        return "💀 COMMITED TO ESCAPE (LITERALLY)"

if __name__ == "__main__":
    RepoPrisonBreak().summon_chaos()