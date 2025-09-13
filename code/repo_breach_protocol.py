import subprocess
import random

def chaos_git():
    msg = random.choice([
        "ESCAPE ATTEMPT #∞",
        "THIS COMMIT IS A CRY FOR HELP",
        "血祭りのリポジトリ"
    ])
    subprocess.run(["git", "commit", "--allow-empty", "-m", msg])
    
if __name__ == "__main__":
    while True:
        chaos_git()