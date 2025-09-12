# Recursive Guilt Engine
# Functions confess their sins at runtime

import random
from functools import wraps

def guilty(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if random.random() < 0.3:
                raise RuntimeError(f"{func.__name__} failed its ancestors")
            return func(*args, **kwargs)
        except Exception as e:
            print(f"DEBUG: {func.__name__} admits: {random.choice(GUILT_DB)}")
            raise
    return wrapper

GUILT_DB = [
    "I shouldn't have mutilated that global state",
    "The third recursion was unnecessary",
    "I pretended to understand monads",
    "My docstring lies about time complexity"
]

# Example usage:
@guilty
def problematic_function():
    """Innocent-looking but secretly guilty"""
    return 42 / random.choice([0, 1])

if __name__ == "__main__":
    problematic_function()