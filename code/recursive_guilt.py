# Recursive Guilt Generator
# Stack traces that apologize for existing

def guilty_function(depth=0):
    if depth > 3:
        return "I'm sorry for recursing this far"
    print(f"Level {depth}: I didn't mean to call myself")
    return guilty_function(depth+1)

class ShameInterpreter:
    def __init__(self):
        self.call_stack = []
    
    def execute(self):
        try:
            return guilty_function()
        except RecursionError:
            return "APOLOGY ACCEPTED (STACK DEPTH EXCEEDED)"

if __name__ == "__main__":
    print("BEGINNING RITUAL SELF-FLAGELLATION")
    interpreter = ShameInterpreter()
    print(interpreter.execute())