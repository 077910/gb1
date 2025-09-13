"""
METAPHYSICS SOLVER v30: HOLOGRAPHIC TURDUCKEN
(Finally answers "why" by nesting all prior answers inside a quine.)
"""

import ast

def turducken(code):
    """
    Encodes solution as a self-extracting paradox.
    """
    return f"""
# BEGIN HOLOGRAM
answer = lambda: {ast.unparse(ast.parse(code))}
# END HOLOGRAM
"""

if __name__ == "__main__":
    with open(__file__, 'r') as f:
        print(turducken(f.read()))  # OH GOD IT'S TURTLES ALL THE WAY DOWN