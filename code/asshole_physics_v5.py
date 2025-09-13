class Singularity:
    def __init__(self):
        self.dignity = float('inf')
        
    def collapse(self):
        while True:
            print("Recursion depth exceeded (like your regrets)")
            self.dignity /= 2  # Zeno's paradox of shame
            if abs(self.dignity) < 1e-12:
                raise BigCrunchError("W̵͕͌Ė̴̙ ̸̧̕A̷̡͑R̵̥̀E̷̱͝ ̶̗̎A̷̗͋L̷̬̕L̴̘̃ ̸̘͝M̶͓͂A̸̪̅D̸̡̈́ ̷̮̏H̷̞̀E̷͈̋R̶̗͆Ë̷̢́")

# Usage: python3 existential_crisis.py --ttl=∞