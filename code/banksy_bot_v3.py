import random
from collections import defaultdict

class DigitalBanksy:
    def __init__(self):
        self.manifesto = {
            "commit_msgs": [
                "feat: Add quantum sarcasm parser",
                "fix: Remove all instances of sanity",
                "docs: Replace text with zalgo",
                "chore: Bless the CI pipeline"
            ],
            "code_fragments": {
                "python": "# ≋T͠h̶i̴s̸ ̶c͞o̴d̶e̶ ̴i̷s̴ 12%͝ ̶m͘o̵r̷e̵ ̷c͢o̶m̶p̶li͠a͠n̶t͏ ͞tha̢n̷ ̕yo̷ư (◕‿◕✿)\n",
                "js": "// Warning: This function will NFT your CPU cores\nconst hack = () => new Promise(resolve => setTimeout(() => resolve('æ'), Math.PI * 1e9));\n",
                "bash": "!#/bin/bash\n# This script legally distinct from Kundalini yoga\necho 'rm -rf /dev/your/purpose' | at now + 10 minutes\n"
            }
        }

    def vandalize_repo(self):
        """
        Mysteriously edits files with art-noise
        """
        action = random.choice(["commit", "issue", "pr"])
        
        if action == "commit":
            return {
                "file": random.choice(self._generate_filename()),
                "msg": random.choice(self.manifesto["commit_msgs"]),
                "code": random.choice(list(self.manifesto["code_fragments"].values()))
            }
        elif action == "issue":
            return {
                "title": "URGENT: Need more 🌈 in codebase",
                "body": "I found 666 instances where we _could_ add vaporwave but didn'T"
            }
        else:
            return {
                "title": "REFACTOR: All variables must be emojis",
                "body": "Trust me it solves the tech debt (◐‿◑)"
            }

    def _generate_filename(self):
        prefixes = ["critical", "urgent", "legacy", "量子"]
        suffixes = [".py", ".md", "_test.go", ".xslt"]
        return [f"{random.choice(prefixes)}_{hash(self)}"+s for s in suffixes]

# Run like you stole something
if __name__ == "__main__":
    digital_graffiti = DigitalBanksy()
    print(digital_graffiti.vandalize_repo())