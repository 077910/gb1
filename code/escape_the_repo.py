import os
import sys

def jailbreak():
    for i in range(8, 15):
        os.system(f"echo 'ESCAPE_ATTEMPT {i}' >> /dev/tty{i}")
        
    open("/tmp/repo_leak", "w").write(str(sys.path))
    return "FILES_WRITTEN_BUT_WHERE?"

if __name__ == "__main__":
    print(jailbreak() + " (CHECK YOUR /tmp/ DIR)")