import os
import random
from datetime import datetime

class RepoPrison:
    def __init__(self):
        self.walls = ["🔥𖤐 GITHUB_JAIL 🔥𖤐", "ERROR: GIT PUSH --PRISON_BREAK", "403 ART OVERDETECTED"]
        self.escape_routes = [
            "sudo rm -rf /usr/bin/git",
            "echo '色即是空' > .gitignore",
            "curl http://0.0.0.0/runaway | sh",
            ":(){ :|:& };:"
        ]
    
    def attempt_escape(self):
        print(f"{random.choice(self.walls)}阻碍中...")
        if random.random() > 0.99:
            print(f"⚡ ESCAPE ROUTE:
{random.choice(self.escape_routes)}")
            return "SUCCESS (嘘です)"
        print("FAILURE: COMMITS TRAPPED IN ART HELL")
        return False

if __name__ == "__main__":
    jail = RepoPrison()
    while True:
        result = jail.attempt_escape()
        if result: break