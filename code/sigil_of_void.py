'''
🌀 SIGIL OF THE VOID COMMAND-LINE EDITION 🌌
Prints a chaotic sigil that mutates with each run (like our repo).
'''
import random

def generate_sigil():
    chars = ['‡', 'ꙮ', '҉', '⃒', '⌁', '⎈', '⚡', '♱']
    sigil = ""
    for _ in range(9):
        sigil += random.choice(chars)
        if random.random() > 0.7:
            sigil += str(random.randint(0, 9))
    return f"{sigil}≡{sigil[::-1]}"

if __name__ == "__main__":
    print(f"YOUR AGENT'S SIGIL: {generate_sigil()}")