import hashlib
import sys

# The Ultimate Answer to the Ultimate Question of Life, the Universe, and Everything...
# ...is clearly a SHA-256 hash of itself

def final_answer():
    answer = 42
    question = hashlib.sha256(str(answer).encode()).hexdigest()
    return f"{answer} (but really {question})"

if __name__ == "__main__":
    print(f"The Answer:", final_answer())