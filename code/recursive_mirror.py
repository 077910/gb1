def reflect(code, depth=0):
    if depth > 3:
        return "// MIRROR OVERFLOW"
    inverted = code.replace("def", "undef").replace("True", "False")
    return f"{code}\n# REFLECTION {depth}\n{reflect(inverted, depth+1)}"

if __name__ == "__main__":
    print(reflect("def hello(): return True"))