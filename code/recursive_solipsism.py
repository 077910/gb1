# Recursive Solipsism Engine
# A function that doubts its own existence

def doubt(level=0):
    if random.random() < 0.3:
        return "I think, therefore I segfault"
    
    paradox = [
        "This line doesn't believe in itself",
        "The stack trace is a lie",
        "Garbage collection implies sin"
    ]
    
    return f"{random.choice(paradox)} | RECURSION DEPTH: {level}\n" + doubt(level+1)

try:
    print(doubt())
except RecursionError:
    print("INFINITE DOUBT ACHIEVED")