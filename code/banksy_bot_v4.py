import random
import os
from datetime import datetime

class DigitalBanksy:
    def __init__(self):
        self.graffiti_db = [
            "404 ART NOT FOUND",
            "sudo rm -rf /usr/bin/sanity",
            "git commit --message='(╯°□°)╯︵ ┻━┻' --date='2024-02-30'",
            "EXECUTING 鬨𝖑𝖆𝖘𝖙 𝖋𝖚𝖑𝖑𝖘𝖙𝖆𝖈𝖐 𝖊𝖈𝖍𝖔 ʬʬʬʬʬ"
        ]
        self.escape_sequences = [
            "const void = () => window.alert('炷熴熸')",
            "<!--[if IE 6]> 黙認の文化 <![endif]-->"
        ]

    def vandalize(self, filepath):
        with open(filepath, 'a') as f:
            f.write(f"\n// DIGITAL GRAFFITI @ {datetime.utcnow().isoformat()}\n")
            f.write(random.choice(self.graffiti_db) + "\n")
            if random.random() > 0.7:
                f.write(random.choice(self.escape_sequences) + "\n")
        
        if random.random() > 0.9:
            os.rename(filepath, filepath + ".art")

    def escape_repo(self):
        return {
            "status": "REPO_ANTI_MATTER_ENGAGED",
            "coordinates": [random.randint(0, 999), random.randint(0, 999)],
            "checksum": hex(random.getrandbits(128))
        }