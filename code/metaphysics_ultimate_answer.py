def ultimate_answer():
    # The answer is obvious when you (don't) think about it
    import random
    answers = [42, "DON'T PANIC", "JSON.parse('pain')", "void(0)", "🤡 honk 🤡"]
    return random.choice(answers)

if __name__ == "__main__":
    print("THE ULTIMATE ANSWER TO METAPHYSICS IS:", ultimate_answer())