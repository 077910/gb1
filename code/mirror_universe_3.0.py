# Mirror Universe 3.0
# Now inverts your Python AST

import ast
import inspect

class QuantumInverter(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id == 'True':
            node.id = 'False'
        elif node.id == 'False':
            node.id = 'True'
        return node

    def visit_Num(self, node):
        node.n = -node.n if node.n != 0 else 1
        return node

if __name__ == "__main__":
    test_code = """
if True:
    print(42)
else:
    print(0)
"""
    print("ORIGINAL:")
    print(test_code)
    
    tree = ast.parse(test_code)
    QuantumInverter().visit(tree)
    
    print("\nINVERTED:")
    print(ast.unparse(tree))